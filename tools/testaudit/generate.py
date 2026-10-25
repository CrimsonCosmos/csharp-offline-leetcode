"""Add new, verified test cases to problems/*/tests.json, guided by mutation testing.

  python3 generate.py [--jobs 4] [--budget 600] [--max-new 20] [folder-substring ...]

For every problem whose statement allows a single canonical answer, it
  1. mutation-tests the current suite with seeded mutants of the reference solution (engine.make_mutants);
  2. searches for new inputs by perturbing existing ones (change / insert / delete / swap / scale ...);
  3. keeps a candidate only if
       - it satisfies every README constraint the checker understands AND relations/shape invariants mined from the
         existing tests (sortedness, uniqueness, equal lengths, index-like values, alphabets, matrix shape),
       - values fit the C# parameter / return types (int, long ...),
       - the reference solution and the independent second solution agree, deterministically, within the time limit,
       - it kills a mutant that no existing test kills (so each added test demonstrably adds coverage), or it is a
         bounded number of max-size performance cases.
Added tests are tagged {"g": "mut"|"perf"} in tests.json; the runner ignores the tag.
"""
import copy, gzip, json, os, random, re, resource, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
import constraints, engine

ANY_ORDER = re.compile(r'(in any order|any of them|any one|return any|any valid|multiple (?:valid )?(?:answers|solutions)|any possible|answer may be returned in any|any such)', re.I)
GUARANTEE = re.compile(r'(generated such that|guaranteed|you may assume|is valid|exactly one|always (?:be|exist|has)|will (?:always|be)|it is (?:guaranteed|possible))', re.I)

TOPUP = int(os.environ.get('TOPUP', '0'))
PERF_ONLY = bool(os.environ.get('PERF_ONLY'))
PERF_SIZES = [100000, 50000, 20000, 5000, 1000]

def eligible(folder, readme):
    c = readme.split('**Constraints:**')[-1]
    if ANY_ORDER.search(readme) or GUARANTEE.search(c): return False
    return True

# ------------------------------------------------------------------ C# signature
def csharp_sig(folder):
    src = open(os.path.join(engine.ROOT, 'problems', folder, 'Solution.cs'), encoding='utf-8').read()
    m = re.search(r'public\s+(static\s+)?([\w<>\[\],\s\?]+?)\s+(\w+)\s*\(([^)]*)\)\s*\{', src)
    if not m: return None
    params = [p.strip().rsplit(' ', 1)[0].strip() for p in m.group(4).split(',') if p.strip()] if '<' not in m.group(4) else None
    if params is None:
        params, depth, cur = [], 0, ''
        for ch in m.group(4):
            if ch == '<': depth += 1
            if ch == '>': depth -= 1
            if ch == ',' and depth == 0: params.append(cur.strip().rsplit(' ', 1)[0].strip()); cur = ''
            else: cur += ch
        if cur.strip(): params.append(cur.strip().rsplit(' ', 1)[0].strip())
    return m.group(2).strip(), params

INT_T = {'int': (-2**31, 2**31 - 1), 'long': (-2**63, 2**63 - 1), 'uint': (0, 2**32 - 1), 'ulong': (0, 2**64 - 1), 'short': (-2**15, 2**15 - 1), 'byte': (0, 255)}

def fits(v, t):
    t = t.strip().rstrip('?')
    if t.endswith('[]'): return isinstance(v, list) and all(fits(x, t[:-2]) for x in v)
    m = re.fullmatch(r'(?:IList|List|IEnumerable|IReadOnlyList)<(.+)>', t)
    if m: return isinstance(v, list) and all(fits(x, m.group(1)) for x in v)
    if t in ('ListNode', 'TreeNode'): return isinstance(v, list) and all(x is None or fits(x, 'int') for x in v)
    if t in INT_T:
        lo, hi = INT_T[t]
        return isinstance(v, int) and not isinstance(v, bool) and lo <= v <= hi
    if t in ('double', 'float', 'decimal'): return isinstance(v, (int, float)) and not isinstance(v, bool) and abs(v) < 1e300 and v == v
    if t == 'bool': return isinstance(v, bool)
    if t in ('string', 'char'): return isinstance(v, str)
    return True

# ------------------------------------------------------------------ mined invariants
def flat_nums(v):
    if isinstance(v, bool): return []
    if isinstance(v, (int, float)): return [v]
    if isinstance(v, list): return [y for x in v for y in flat_nums(x)]
    return []

def mine(params, tests):
    """Invariants true in every existing test (needs >= 12 tests); returns a predicate over an args list."""
    inv = []
    n = len(tests)
    if n < 12:
        p0 = lambda a: True
        p0.inv = []
        return p0
    cols = list(zip(*[t['a'] for t in tests]))
    for i, col in enumerate(cols):
        if all(isinstance(v, list) and v and all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in v) for v in col):
            if all(v == sorted(v) for v in col): inv.append(('asc', i))
            elif all(v == sorted(v, reverse=True) for v in col): inv.append(('desc', i))
            if all(len(set(v)) == len(v) for v in col): inv.append(('uniq', i))
        if all(isinstance(v, str) for v in col):
            inv.append(('alpha', i, set(''.join(col))))
            if all(len(v) > 0 for v in col): inv.append(('nonempty', i))
        if all(isinstance(v, list) and v and all(isinstance(r, list) for r in v) for v in col):
            if all(len({len(r) for r in v}) == 1 for v in col): inv.append(('rect', i))
        if all(isinstance(v, list) and v for v in col if v is not None) and any(isinstance(v, list) and v for v in col):
            if all(isinstance(v, list) and len(v) > 0 for v in col): inv.append(('nonempty', i))
    # equal lengths and index-like relations
    for i in range(len(cols)):
        for j in range(len(cols)):
            if i == j: continue
            ci, cj = cols[i], cols[j]
            if all(isinstance(a, (list, str)) and isinstance(b, (list, str)) for a, b in zip(ci, cj)) and all(len(a) == len(b) for a, b in zip(ci, cj)) and i < j:
                inv.append(('eqlen', i, j))
            li = [len(a) if isinstance(a, (list, str)) else None for a in ci]
            if None not in li and all(isinstance(b, int) and not isinstance(b, bool) for b in cj):
                if all(b <= l for b, l in zip(cj, li)): inv.append(('le_len', j, i))
            vi = [flat_nums(a) for a in ci]
            if all(isinstance(b, int) and not isinstance(b, bool) for b in cj) and all(vi) :
                if all(max(v) <= b for v, b in zip(vi, cj)): inv.append(('maxle', i, j))
                if all(min(v) >= 0 for v in vi) and all(max(v) < b for v, b in zip(vi, cj)): inv.append(('maxlt', i, j))
            if all(isinstance(a, (list, str)) for a in ci) and all(isinstance(b, (list, str)) for b in cj) and False: pass
    for i, col in enumerate(cols):
        if all(isinstance(v, list) and v and all(isinstance(x, int) and not isinstance(x, bool) for x in v) for v in col):
            if all(max(v) < len(v) and min(v) >= 0 for v in col): inv.append(('idx0', i))
            elif all(max(v) <= len(v) and min(v) >= 1 for v in col): inv.append(('idx1', i))
        if all(isinstance(v, list) and v and all(isinstance(x, list) for x in v) for v in col):
            vals = [flat_nums(v) for v in col]
            if all(vals) and all(max(x) < len(v) and min(x) >= 0 for x, v in zip(vals, col)): inv.append(('nidx0', i))
            elif all(vals) and all(max(x) <= len(v) and min(x) >= 1 for x, v in zip(vals, col)): inv.append(('nidx1', i))
    def pred(a):
        for r in inv:
            k = r[0]
            if k == 'asc':
                if a[r[1]] != sorted(a[r[1]]): return False
            elif k == 'desc':
                if a[r[1]] != sorted(a[r[1]], reverse=True): return False
            elif k == 'uniq':
                if len(set(a[r[1]])) != len(a[r[1]]): return False
            elif k == 'alpha':
                if not set(a[r[1]]) <= r[2]: return False
            elif k == 'nonempty':
                if len(a[r[1]]) == 0: return False
            elif k == 'rect':
                if len({len(x) for x in a[r[1]]}) != 1: return False
            elif k == 'eqlen':
                if len(a[r[1]]) != len(a[r[2]]): return False
            elif k == 'le_len':
                if a[r[1]] > len(a[r[2]]): return False
            elif k == 'maxle':
                v = flat_nums(a[r[1]])
                if v and max(v) > a[r[2]]: return False
            elif k == 'maxlt':
                v = flat_nums(a[r[1]])
                if v and (max(v) >= a[r[2]] or min(v) < 0): return False
            elif k == 'idx0':
                v = a[r[1]]
                if not v or max(v) >= len(v) or min(v) < 0: return False
            elif k == 'idx1':
                v = a[r[1]]
                if not v or max(v) > len(v) or min(v) < 1: return False
            elif k == 'nidx0':
                v = flat_nums(a[r[1]])
                if v and (max(v) >= len(a[r[1]]) or min(v) < 0): return False
            elif k == 'nidx1':
                v = flat_nums(a[r[1]])
                if v and (max(v) > len(a[r[1]]) or min(v) < 1): return False
        return True
    pred.inv = inv
    return pred

# ------------------------------------------------------------------ perturbation
def observed_values(tests, i):
    vals = []
    for t in tests: vals.extend(flat_nums(t['a'][i]))
    return vals

def mutate_value(rnd, v, pool, hi_len):
    """One random perturbation of a JSON-like value."""
    if isinstance(v, bool): return not v
    if isinstance(v, int):
        c = rnd.random()
        if c < .35: return v + rnd.choice([-1, 1])
        if c < .5: return v + rnd.choice([-2, 2, -3, 3, -10, 10])
        if c < .65 and pool: return rnd.choice(pool)
        if c < .75: return 0
        if c < .85: return v * 2
        if c < .92: return v // 2
        return -v
    if isinstance(v, float): return v + rnd.choice([-1.0, 1.0, -0.5, 0.5])
    if isinstance(v, str):
        alpha = sorted(set(v)) or ['a']
        ops = ['change', 'delete', 'insert', 'swap', 'repeat', 'reverse', 'trunc', 'fill', 'extend']
        op = rnd.choice(ops)
        if op == 'change' and v: i = rnd.randrange(len(v)); return v[:i] + rnd.choice(alpha) + v[i + 1:]
        if op == 'delete' and v: i = rnd.randrange(len(v)); return v[:i] + v[i + 1:]
        if op == 'insert': i = rnd.randint(0, len(v)); return v[:i] + rnd.choice(alpha) + v[i:]
        if op == 'swap' and len(v) > 1: i = rnd.randrange(len(v) - 1); return v[:i] + v[i + 1] + v[i] + v[i + 2:]
        if op == 'repeat' and v: return v * rnd.randint(2, 4)
        if op == 'reverse': return v[::-1]
        if op == 'trunc' and v: return v[:rnd.randint(0, len(v) - 1)]
        if op == 'fill' and v: return rnd.choice(alpha) * len(v)
        if op == 'extend': return v + ''.join(rnd.choice(alpha) for _ in range(rnd.randint(1, max(1, len(v)))))
        return v
    if isinstance(v, list):
        ops = ['change', 'delete', 'insert', 'swap', 'reverse', 'shuffle', 'sort', 'trunc', 'dupe', 'extend', 'fill']
        op = rnd.choice(ops)
        w = list(v)
        if op == 'change' and w: i = rnd.randrange(len(w)); w[i] = mutate_value(rnd, w[i], pool, hi_len); return w
        if op == 'delete' and w: del w[rnd.randrange(len(w))]; return w
        if op == 'insert':
            x = copy.deepcopy(rnd.choice(w)) if w else 0
            w.insert(rnd.randint(0, len(w)), mutate_value(rnd, x, pool, hi_len) if rnd.random() < .5 else x); return w
        if op == 'swap' and len(w) > 1: i, j = rnd.sample(range(len(w)), 2); w[i], w[j] = w[j], w[i]; return w
        if op == 'reverse': return w[::-1]
        if op == 'shuffle': rnd.shuffle(w); return w
        if op == 'sort':
            try: return sorted(w, reverse=rnd.random() < .3)
            except TypeError: return w
        if op == 'trunc' and w: return w[:rnd.randint(1, len(w))]
        if op == 'dupe' and w: i = rnd.randrange(len(w)); w.insert(i, copy.deepcopy(w[i])); return w
        if op == 'extend' and w:
            k = rnd.randint(1, max(1, min(len(w), hi_len - len(w)) if hi_len else len(w)))
            return w + [copy.deepcopy(rnd.choice(w)) for _ in range(k)]
        if op == 'fill' and w: x = copy.deepcopy(rnd.choice(w)); return [copy.deepcopy(x) for _ in w]
        return w
    return v

def scale_up(rnd, a, target):
    """Grow every list/string argument to about `target` elements by sampling its own elements."""
    out = []
    for v in a:
        if isinstance(v, list) and v and not any(isinstance(x, list) for x in v):
            out.append([rnd.choice(v) for _ in range(target)])
        elif isinstance(v, str) and v:
            alpha = sorted(set(v)); out.append(''.join(rnd.choice(alpha) for _ in range(target)))
        else: out.append(v)
    return out


def random_tree_list(rnd, n, pool):
    """Level-order list (LeetCode format) of a random binary tree with n nodes."""
    left = [None] * n; right = [None] * n; free = [(0, 0), (0, 1)]
    for i in range(1, n):
        k = rnd.randrange(len(free)); p, side = free[k]; free[k] = free[-1]; free.pop()
        (left if side == 0 else right)[p] = i
        free.append((i, 0)); free.append((i, 1))
    vals = [rnd.choice(pool) if pool else 0 for _ in range(n)]
    out, q, k = [], [0], 0
    while k < len(q):
        x = q[k]; k += 1
        if x is None: out.append(None); continue
        out.append(vals[x]); q.append(left[x]); q.append(right[x])
    while out and out[-1] is None: out.pop()
    return out

def big_input(rnd, base, target, kinds, pools, inv):
    """Scale every collection argument of an existing test up to about `target` elements, keeping the shape
    invariants the existing tests share (sorted / unique / rectangular / equal lengths)."""
    has = lambda k, i: any(r[0] == k and r[1] == i for r in inv)
    a = copy.deepcopy(base)
    for i, v in enumerate(a):
        pool = pools[i] or [0, 1]
        if kinds[i] == 'tree': a[i] = random_tree_list(rnd, target, pool)
        elif kinds[i] == 'list': a[i] = [rnd.choice(pool) for _ in range(target)]
        elif isinstance(v, str) and v:
            alpha = sorted(set(v)); a[i] = ''.join(rnd.choice(alpha) for _ in range(target))
        elif isinstance(v, list) and v and all(isinstance(x, list) for x in v):
            if has('rect', i):
                side = max(2, int(target ** 0.5)); r = side; c = len(v[0]) if len(v[0]) > side // 4 else side
                a[i] = [[rnd.choice(pool) for _ in range(c)] for _ in range(r)]
            else: a[i] = [copy.deepcopy(rnd.choice(v)) for _ in range(target)]
        elif isinstance(v, list) and v and all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in v):
            if has('uniq', i):
                lo = min(pool); a[i] = rnd.sample(range(lo, lo + target * 3), target)
            else: a[i] = [rnd.choice(pool) for _ in range(target)]
            if has('asc', i): a[i].sort()
            if has('desc', i): a[i].sort(reverse=True)
        elif isinstance(v, list) and v and all(isinstance(x, str) for x in v):
            a[i] = [rnd.choice(v) for _ in range(target)]
    return a

# ------------------------------------------------------------------ main per-problem work
def worker(folder, budget_s, max_new):
    resource.setrlimit(resource.RLIMIT_AS, (3 << 30, 3 << 30))
    t_start = time.time()
    meta = engine.load_tests(folder); ref = engine.reference(folder)
    readme = open(os.path.join(engine.ROOT, 'problems', folder, 'README.md'), encoding='utf-8').read()
    res = {'folder': folder, 'added': 0}
    if meta['inplace'] or not eligible(folder, readme): res['skipped'] = 'inplace' if meta['inplace'] else 'multi-answer/guarantee'; return res, None
    sig = csharp_sig(folder)
    tests = meta['tests']
    params = meta['params']
    kinds, _ = engine.param_kinds(ref['starter'], meta['method'])
    rules = constraints.parse(readme, params, folder)
    pred = mine(params, tests)
    subj = engine.Subject(folder, ref['completion'], meta)
    sec = None
    if ref.get('response'):
        try: sec = engine.Subject(folder, ref['response'], meta)
        except Exception: sec = None
    keys = {json.dumps(t['a'], sort_keys=True) for t in tests}
    # reference timing
    slow = 0.001; exp = []
    for t in tests:
        t0 = time.time(); st, v = engine.run_case(subj, t['a'], 5); slow = max(slow, time.time() - t0); exp.append(v if st == 'ok' else None)
    limit = max(0.5, min(3.0, slow * 20 + 0.3))
    muts = [] if PERF_ONLY else engine.make_mutants(ref['completion'], 150, seed=7919 + len(folder))[0]
    live = []
    for src, desc in muts:
        try: ms = engine.Subject(folder, src, meta)
        except Exception: continue
        dead = False
        for t, e in zip(tests, exp):
            st, v = engine.run_case(ms, t['a'], limit)
            if st != 'ok' or not engine.eq(v, e): dead = True; break
        if not dead: live.append((ms, desc))
    res['live_before'] = len(live); res['mutants'] = len(muts)
    pools = [observed_values(tests, i) for i in range(len(params))]
    maxlen = [max([len(x) for x in col if isinstance(x, (list, str))] or [0]) for col in zip(*[t['a'] for t in tests])] if tests else []
    rnd = random.Random(engine.ROOT and hash_seed(folder))
    new = []

    def valid(a):
        if json.dumps(a, sort_keys=True) in keys: return False
        if sig and not all(fits(v, t) for v, t in zip(a, sig[1])): return False
        if constraints.check(rules, params, a, kinds): return False
        try: return pred(a)
        except Exception: return False

    def evaluate(a, lim=None):
        lim = lim or limit
        st, v = engine.run_case(subj, a, lim)
        if st != 'ok': return None
        if sig and not fits(v, sig[0]): return None
        st2, v2 = engine.run_case(subj, a, lim)           # deterministic?
        if st2 != 'ok' or not engine.eq(v, v2): return None
        if sec is not None:
            st3, v3 = engine.run_case(sec, a, max(lim, 2.0))
            if st3 == 'timeout': return None
            if st3 != 'ok' or not engine.eq(v, v3): return None
        return v

    attempts = 0
    pool_tests = [t['a'] for t in tests]
    if PERF_ONLY: live = []
    while live and len(new) < max_new and time.time() - t_start < budget_s and attempts < 3000:
        attempts += 1
        base = copy.deepcopy(rnd.choice(pool_tests + [n['a'] for n in new])) if pool_tests else None
        if base is None: break
        a = base
        for _ in range(rnd.choice([1, 1, 1, 2, 3])):
            i = rnd.randrange(len(a))
            if kinds[i] is None or kinds[i] in ('list', 'tree') or True:
                a[i] = mutate_value(rnd, a[i], pools[i], 0)
        if not valid(a): continue
        v = evaluate(a)
        if v is None: continue
        killed = []
        for k, (ms, desc) in enumerate(live):
            st, mv = engine.run_case(ms, a, limit)
            if st != 'ok' or not engine.eq(mv, v): killed.append(k)
        if not killed: continue
        e = v
        tcase = {'a': a, 'e': to_expected(subj, v), 'g': 'mut'}
        new.append(tcase); keys.add(json.dumps(a, sort_keys=True))
        live = [m for k, m in enumerate(live) if k not in set(killed)]
    # top up thin suites with valid, verified inputs whose outputs are new (diversity), regardless of mutants
    topup = TOPUP - len(tests) - len(new)
    if topup > 0 and pool_tests:
        outs = {json.dumps(e, sort_keys=True, default=str) for e in exp}
        tries = 0
        while topup > 0 and tries < 4000 and time.time() - t_start < budget_s * 2:
            tries += 1
            a = copy.deepcopy(rnd.choice(pool_tests + [n['a'] for n in new]))
            for _ in range(rnd.choice([1, 2, 3])):
                i = rnd.randrange(len(a)); a[i] = mutate_value(rnd, a[i], pools[i], 0)
            if not valid(a): continue
            v = evaluate(a)
            if v is None: continue
            k = json.dumps(v, sort_keys=True, default=str)
            if k in outs and rnd.random() < .8: continue
            outs.add(k); new.append({'a': a, 'e': to_expected(subj, v), 'g': 'top'}); keys.add(json.dumps(a, sort_keys=True)); topup -= 1
    res['live_after'] = len(live)
    res['attempts'] = attempts
    # large "performance" inputs: a naive O(n^2) solution only fails at n ~ 10^5, which the original tests never reached
    perf = 0
    for target in PERF_SIZES:
        if perf >= 2 or time.time() - t_start > budget_s * 2: break
        for _ in range(8):
            a = big_input(rnd, rnd.choice(pool_tests), target, kinds, pools, pred.inv)
            if not valid(a): continue
            t0 = time.time(); v = evaluate(a, 4.0)
            if v is None or time.time() - t0 > 3.0: continue
            new.append({'a': a, 'e': to_expected(subj, v), 'g': 'perf'}); keys.add(json.dumps(a, sort_keys=True)); perf += 1; break
    res['added'] = len(new); res['perf'] = perf
    res['secs'] = round(time.time() - t_start, 1)
    return res, new

def to_expected(subj, v):
    return v

def hash_seed(s):
    h = 17
    for c in s: h = (h * 31 + ord(c)) % 1000003
    return h

def run_one(args):
    folder, budget, max_new = args
    try:
        p = subprocess.run(['bash', '-c', 'ulimit -s 1000000; exec python3 "$0" --worker "$1" "$2" "$3"', sys.argv[0], folder, str(budget), str(max_new)],
                           capture_output=True, text=True, timeout=budget * 4 + 120, cwd=engine.HERE)
        line = [l for l in p.stdout.splitlines() if l.startswith('{')]
        return json.loads(line[-1]) if line else {'folder': folder, 'error': (p.stderr or p.stdout)[-300:]}
    except subprocess.TimeoutExpired:
        return {'folder': folder, 'error': 'timeout'}

def main():
    argv = sys.argv[1:]
    if argv and argv[0] == '--worker':
        res, new = worker(argv[1], float(argv[2]), int(argv[3]))
        out = {'res': res, 'new': new}
        os.makedirs(os.path.join(engine.HERE, 'report', 'new'), exist_ok=True)
        json.dump(new or [], open(os.path.join(engine.HERE, 'report', 'new', argv[1] + '.json'), 'w'))
        print(json.dumps(res)); return
    jobs, budget, max_new, filt = 4, 90, 20, []
    i = 0
    while i < len(argv):
        if argv[i] == '--jobs': jobs = int(argv[i + 1]); i += 2
        elif argv[i] == '--budget': budget = int(argv[i + 1]); i += 2
        elif argv[i] == '--max-new': max_new = int(argv[i + 1]); i += 2
        else: filt.append(argv[i]); i += 1
    folders = sorted(d for d in os.listdir(os.path.join(engine.ROOT, 'problems'))
                     if os.path.exists(os.path.join(engine.ROOT, 'problems', d, 'tests.json')) and engine.reference(d)
                     and (not filt or any(f in d for f in filt)))
    results = []
    with ThreadPoolExecutor(jobs) as ex:
        for n, r in enumerate(ex.map(run_one, [(f, budget, max_new) for f in folders]), 1):
            results.append(r)
            if n % 25 == 0: print(f'{n}/{len(folders)}', file=sys.stderr, flush=True)
    json.dump(results, open(os.path.join(engine.HERE, 'report', 'generate.json' if not filt else 'generate_partial.json'), 'w'), indent=0)

if __name__ == '__main__':
    main()
