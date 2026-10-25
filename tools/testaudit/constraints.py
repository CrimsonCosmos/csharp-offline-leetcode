"""Check test inputs against the constraints written in each problem's README.

Only a conservative subset is understood (numeric bounds on a parameter, its length, its elements or its nested
elements; node counts / node values for ListNode & TreeNode inputs; lowercase/uppercase/digit alphabets; unique;
sorted). Superscripts were flattened when the READMEs were created ("10^4" became "104", "2^31 - 1" became
"231 - 1"), so a bound token can mean either reading; the MORE PERMISSIVE reading is used, so a test is flagged only
when it violates the constraint under every reading.
"""
import json, math, os, re
import engine

NUM = r'-?\d+(?:\s*[*+-]\s*\d+)*'

def readings(tok):
    """All plausible values of one integer token as written in the README (see module docstring)."""
    neg = tok.startswith('-'); t = tok.lstrip('-')
    vals = {int(t)}
    if re.fullmatch(r'10\d{1,2}', t) and 3 <= int(t[2:]) <= 18: vals.add(10 ** int(t[2:]))
    if re.fullmatch(r'2\d{1,2}', t) and 10 <= int(t[1:]) <= 63: vals.add(2 ** int(t[1:]))
    return [-v if neg else v for v in vals]

def bound_values(expr):
    """Evaluate e.g. '2 * 104', '231 - 1', '-109' under every reading -> list of candidate values."""
    expr = expr.strip()
    parts = re.split(r'\s*([*+-])\s*(?=\d)', expr)   # tokens and operators alternate
    # handle a leading unary minus
    toks = []
    m = re.match(r'-?\d+', expr)
    if not m: return []
    first = m.group(0); rest = expr[m.end():]
    seq = [first] + re.findall(r'[*+-]|\d+', rest)
    cands = [[0]]
    # evaluate with precedence * over +/-; small search over readings
    vals = []
    def rec(i, terms, ops):
        if i >= len(seq):
            # apply * first
            t, o = list(terms), list(ops)
            k = 0
            while k < len(o):
                if o[k] == '*': t[k] = t[k] * t[k + 1]; del t[k + 1]; del o[k]
                else: k += 1
            v = t[0]
            for op, x in zip(o, t[1:]): v = v + x if op == '+' else v - x
            vals.append(v); return
        if seq[i] in '*+-' and not seq[i].lstrip('-').isdigit():
            rec(i + 1, terms, ops + [seq[i]]); return
        for r in (readings(seq[i]) if i == 0 else readings(seq[i])):
            rec(i + 1, terms + [r], ops)
    rec(0, [], [])
    return vals

_ACC = re.compile(r'^(\w+?)((?:\[[a-z]\])*)(\.length)?$')   # [i], [j] only: not [0] or [i][i]
class _Acc:
    @staticmethod
    def match(t):
        m = _ACC.match(t.strip())
        if m:
            idx = re.findall(r'\[([a-z])\]', m.group(2))
            if len(set(idx)) != len(idx): return None
        return m
ACC = _Acc

# README lines that are known to be contradicted by the problem's own other constraints (the head's manager is -1).
DROP_LINES = {'1376-time-needed-to-inform-all-employees': ['0 <= manager[i] < n']}

def parse(readme, params, folder=''):
    """-> list of rules. Relational rules are chains of terms joined by <=, < or ==."""
    sec = readme.split('**Constraints:**', 1)
    if len(sec) < 2: return []
    names = set(params)
    lines = []
    for line in sec[1].splitlines():
        line = line.strip().lstrip('-').strip().replace('`', '')
        if line and not line.startswith(('<', '**Follow', '**Example')) and line not in DROP_LINES.get(folder, []): lines.append(line)
    # pass 1: aliases such as "n == nums.length" (n is not a parameter)
    alias = {}
    for line in lines:
        ts = [t.strip() for t in re.split(r'==', line)]
        if len(ts) >= 2 and re.fullmatch(r'\w+', ts[0]) and ts[0] not in names and not ts[0].isdigit() and ' ' not in line.replace(' == ', ''):
            for t in ts[1:]:
                m = ACC.match(t)
                if m and m.group(1) in names and m.group(1) != ts[0]: alias[ts[0]] = t; break
        elif len(ts) >= 2:
            # "1 <= n == nums.length <= 105"
            m = re.fullmatch(r'.*?<=?\s*(\w+)\s*==\s*([\w\[\]\.]+)\s*<=?.*', line)
            if m and m.group(1) not in names and ACC.match(m.group(2)) and ACC.match(m.group(2)).group(1) in names: alias[m.group(1)] = m.group(2)
    rules = []
    def term(t):
        t = t.strip()
        if re.fullmatch(NUM, t): return ('lit', t)
        m = re.fullmatch(r'(\w+)\s*([+-])\s*(\d+)', t)
        if m and (m.group(1) in alias or m.group(1) in names):
            base = term(m.group(1))
            return ('arith', base, m.group(2), int(m.group(3))) if base else None
        if t in alias: t = alias[t]
        m = ACC.match(t)
        if m and m.group(1) in names: return ('acc', m.group(1), m.group(2).count('['), bool(m.group(3)))
        return None
    for line in lines:
        m = re.fullmatch(r'The number of nodes in (?:the )?(?:\w+ )?(?:tree|list|linked list|lists|trees)?.*?\[(\d+),\s*(\d+)\]\.?', line)
        if m: rules.append(('nodes', int(m.group(1)), m.group(2))); continue
        m = re.fullmatch(r'(-?\d+(?:\s*[*+-]\s*\d+)*)\s*<=\s*Node\.val\s*<=\s*(' + NUM + ')', line)
        if m: rules.append(('nodeval', m.group(1), m.group(2))); continue
        m = re.fullmatch(r'(\w+)(\[\w\])? (?:consists|consist) (?:only )?of (?:only )?(lowercase|uppercase) English letters\.?', line)
        if m and m.group(1) in names: rules.append(('alpha', m.group(1), bool(m.group(2)), m.group(3))); continue
        m = re.fullmatch(r'(\w+)(\[\w\])? (?:consists|consist) (?:only )?of (?:only )?digits\.?', line)
        if m and m.group(1) in names: rules.append(('alpha', m.group(1), bool(m.group(2)), 'digits')); continue
        m = re.fullmatch(r'(\w+) and (\w+) consist (?:only )?of (?:only )?(lowercase|uppercase) English letters\.?', line)
        if m and m.group(1) in names and m.group(2) in names:
            rules.append(('alpha', m.group(1), False, m.group(3))); rules.append(('alpha', m.group(2), False, m.group(3))); continue
        m = re.fullmatch(r'(?:All the |All )?(?:\w+ )?(?:of )?(\w+) (?:are|is) (?:unique|distinct)\.?', line)
        if m and m.group(1) in names: rules.append(('unique', m.group(1))); continue
        m = re.fullmatch(r'(\w+) is sorted in (non-decreasing|ascending|strictly increasing|non-increasing|descending) order\.?', line)
        if m and m.group(1) in names: rules.append(('sorted', m.group(1), m.group(2))); continue
        m = re.fullmatch(r"(\w+(?:\[\w\])*) is either '?(\w)'? or '?(\w)'?\.?", line)
        if m and ACC.match(m.group(1)) and ACC.match(m.group(1)).group(1) in names:
            a = ACC.match(m.group(1)); rules.append(('oneof', a.group(1), a.group(2).count('['), {m.group(2), m.group(3)})); continue
        # --- structural guarantees stated in prose ---------------------------------------------------------
        mm = re.search(r'\b(\w+) is (?:an? |guaranteed to be |sorted and )?(?:ascending |sorted )?(?:array )?(?:that is )?(?:possibly |guaranteed to be )?rotated', line)
        if mm and mm.group(1) in names: rules.append(('rotated', mm.group(1))); continue
        mm = re.fullmatch(r'(\w+) is sorted and rotated.*', line)
        if mm and mm.group(1) in names: rules.append(('rotated', mm.group(1))); continue
        mm = re.fullmatch(r'(\w+) is (?:a )?(non-decreasing|non-increasing|sorted|ascending) (?:array|list)\.?', line)
        if mm and mm.group(1) in names: rules.append(('sorted', mm.group(1), 'non-increasing' if mm.group(2) == 'non-increasing' else 'non-decreasing')); continue
        mm = re.fullmatch(r'(?:The list|(\w+)) is guaranteed to be sorted in (ascending|non-decreasing|descending) order\.?', line)
        if mm:
            tgt = mm.group(1) or next((n for n in names if n in ('head', 'list1')), None)
            if tgt in names: rules.append(('sorted', tgt, 'descending' if mm.group(2) == 'descending' else 'non-decreasing')); continue
        mm = re.fullmatch(r'(\w+) is sorted by \w+ in (ascending|non-decreasing) order\.?', line)
        if mm and mm.group(1) in names: rules.append(('sortedby0', mm.group(1))); continue
        mm = re.fullmatch(r'All the (?:values|integers)(?: of| in)? (?:the )?(?:Node\.val|tree|list|nodes|BST)?\s*(?:are|is) (?:unique|distinct)\.?|All the values Node\.val are unique\.|The values of the nodes in the tree are unique\.|All the values of the tree are unique\.|All the values in the tree are unique\.', line)
        if mm: rules.append(('nodeunique',)); continue
        mm = re.fullmatch(r'All (?:the )?pairs? (?:\[?\w+, ?\w+\]?|\(\w+, ?\w+\)|\w+\[\w\])\s*(?:are|is) (?:unique|distinct)\.?', line)
        if mm:
            tgt = next((n for n in names if n in ('prerequisites', 'edges', 'roads', 'connections', 'flights', 'points', 'times', 'relations')), None)
            if tgt: rules.append(('rowsunique', tgt)); continue
        mm = re.fullmatch(r'There are no (?:repeated|duplicate) edges\.?', line)
        if mm and 'edges' in names: rules.append(('rowsunique', 'edges', True)); continue
        mm = re.fullmatch(r'(\w+)\[i\] != \1\[i \+ 1\] for all valid i\.?', line)
        if mm and mm.group(1) in names: rules.append(('adjdistinct', mm.group(1))); continue
        mm = re.search(r'(?:valid binary search tree|is a BST)', line)
        if mm: rules.append(('bst',)); continue
        mm = re.fullmatch(r'(\w+) represents a valid tree\.?|The input is generated such that (\w+) represents a valid tree\.?', line)
        if mm and (mm.group(1) or mm.group(2)) in names: rules.append(('validtree', mm.group(1) or mm.group(2))); continue
        # relational chain
        if ',' in line and re.search(r'<=?', line):
            m = re.fullmatch(r'(.+?)\s*(<=?)\s*([\w\[\]\.]+(?:\s*,\s*[\w\[\]\.]+)+)\s*(<=?)\s*(.+)', line)
            if m:   # lo <= a, b <= hi
                group = [term(x) for x in m.group(3).split(',')]
                lo, hi = term(m.group(1)), term(m.group(5))
                if lo and hi and all(group):
                    for g in group: rules.append(('chain', [lo, g, hi], ['<=', '<=']))
                continue
        parts = re.split(r'\s*(<=|<|==)\s*', line)
        terms = [term(p) for p in parts[0::2]]
        ops = parts[1::2]
        if len(terms) >= 2 and all(terms) and any(t[0] != 'lit' for t in terms):
            rules.append(('chain', terms, ops))
    return rules

def evaluate(t, A, K):
    """Numeric values a term takes in a test case, or None if unknown."""
    if t[0] == 'acc':
        _, name, depth, isl = t
        if K.get(name) in ('list', 'tree', 'lists', 'trees'): return None
        items = collect(A.get(name), depth)
        if isl: vals = [len(x) for x in items if isinstance(x, (list, str, tuple))]
        else: vals = [x for x in items if isinstance(x, (int, float)) and not isinstance(x, bool)]
        return vals
    if t[0] == 'arith':
        base = evaluate(t[1], A, K)
        return None if base is None else [x + t[3] if t[2] == '+' else x - t[3] for x in base]
    return None

def collect(v, depth):
    if depth == 0: return [v]
    out = []
    if isinstance(v, (list, tuple)):
        for x in v: out.extend(collect(x, depth - 1))
    return out


def _is_bst(vals):
    """Level-order list (None = missing) -> is it a valid binary search tree (strict)?"""
    if not vals or vals[0] is None: return True
    nodes = [[vals[0], None, None]]; q = [nodes[0]]; i = 1; k = 0
    while k < len(q) and i < len(vals):
        n = q[k]; k += 1
        for side in (1, 2):
            if i < len(vals):
                if vals[i] is not None: c = [vals[i], None, None]; n[side] = c; q.append(c)
                i += 1
    out, st, cur = [], [], nodes[0]
    while cur or st:
        while cur: st.append(cur); cur = cur[1]
        cur = st.pop(); out.append(cur[0]); cur = cur[2]
    return all(a < b for a, b in zip(out, out[1:]))

def _connected(n, edges):
    par = list(range(n))
    def f(x):
        while par[x] != x: par[x] = par[par[x]]; x = par[x]
        return x
    for e in edges:
        a, b = e[0], e[1]
        if not (0 <= a < n and 0 <= b < n): return False
        par[f(a)] = f(b)
    return len({f(x) for x in range(n)}) == 1

def check(rules, params, args, kinds):
    """-> list of violation strings for one test case."""
    A = dict(zip(params, args)); K = dict(zip(params, kinds))
    bad = []
    for r in rules:
        if r[0] == 'chain':
            _, terms, ops = r
            for i, op in enumerate(ops):
                L, R = terms[i], terms[i + 1]
                lv = [min(bound_values(L[1])), max(bound_values(L[1]))] if L[0] == 'lit' else evaluate(L, A, K)
                rv = [min(bound_values(R[1])), max(bound_values(R[1]))] if R[0] == 'lit' else evaluate(R, A, K)
                if lv is None or rv is None or not lv or not rv: continue
                multi = lambda T, V: T[0] == 'acc' and not T[3] and T[2] > 0
                if multi(L, lv) and multi(R, rv): continue          # element-wise relation between two arrays: not modelled
                if op == '==':
                    if L[0] == 'lit': ok = all(any(x == v for v in bound_values(L[1])) for x in rv)
                    elif R[0] == 'lit': ok = all(any(x == v for v in bound_values(R[1])) for x in lv)
                    else: ok = len(set(lv)) == 1 and len(set(rv)) == 1 and lv[0] == rv[0]
                else:
                    lo_side = [min(bound_values(L[1]))] if L[0] == 'lit' else lv    # literal lower bound: most permissive reading
                    hi_side = [max(bound_values(R[1]))] if R[0] == 'lit' else rv    # literal upper bound: most permissive reading
                    ok = max(lo_side) <= min(hi_side)
                if not ok:
                    bad.append(f'chain {terms[i][1] if terms[i][0]=="acc" else terms[i]} {op} {terms[i+1][1] if terms[i+1][0]=="acc" else terms[i+1]} violated ({lv[:3]} vs {rv[:3]})'); break
        elif r[0] == 'nodes':
            hi = max(bound_values(r[2]) or [int(r[2])])
            for n, k in K.items():
                if k in ('list', 'tree'):
                    cnt = len([x for x in A[n] if x is not None]) if A[n] else 0
                    if cnt > hi: bad.append(f'nodes {n}={cnt} > {hi}'); break
        elif r[0] == 'nodeval':
            lo_v, hi_v = min(bound_values(r[1])), max(bound_values(r[2]))
            for n, k in K.items():
                if k in ('list', 'tree') and A[n]:
                    for x in A[n]:
                        if isinstance(x, int) and not isinstance(x, bool) and not (lo_v <= x <= hi_v): bad.append(f'Node.val {x} not in [{lo_v},{hi_v}]'); break
        elif r[0] == 'alpha':
            _, name, nested, kind = r
            rx = {'lowercase': '[a-z]*', 'uppercase': '[A-Z]*', 'digits': '[0-9]*'}[kind]
            for s in collect(A[name], 1 if nested else 0):
                if isinstance(s, str) and not re.fullmatch(rx, s): bad.append(f'alphabet {name}={s[:20]!r} not {kind}'); break
        elif r[0] == 'oneof':
            _, name, depth, allowed = r
            flat = collect(A[name], depth)
            flat = [c for x in flat for c in (x if isinstance(x, str) else [x])]
            for x in flat:
                if str(x) not in allowed: bad.append(f'value {name}={x!r} not one of {sorted(allowed)}'); break
        elif r[0] == 'rotated':
            v = A[r[1]]
            if isinstance(v, list) and v:
                srt = sorted(v)
                if not any(v == srt[k:] + srt[:k] for k in range(len(v))): bad.append(f'{r[1]} is not a rotation of a sorted array')
        elif r[0] == 'sortedby0':
            v = A[r[1]]
            if isinstance(v, list) and all(isinstance(x, list) and x for x in v):
                if any(a[0] > b[0] for a, b in zip(v, v[1:])): bad.append(f'{r[1]} not sorted by start')
        elif r[0] in ('nodeunique', 'bst'):
            for n, k in K.items():
                if k == 'tree' and A[n]:
                    vals = [x for x in A[n] if x is not None]
                    if r[0] == 'nodeunique' and len(set(vals)) != len(vals): bad.append('node values not unique'); break
                    if r[0] == 'bst' and not _is_bst(A[n]): bad.append('tree is not a valid BST'); break
                elif k == 'list' and A[n] and r[0] == 'nodeunique' and len(set(A[n])) != len(A[n]): bad.append('node values not unique'); break
        elif r[0] == 'rowsunique':
            v = A[r[1]]
            if isinstance(v, list) and all(isinstance(x, list) for x in v):
                seen = set()
                for x in v:
                    key = tuple(sorted(x)) if len(r) > 2 else tuple(x)
                    if key in seen: bad.append(f'{r[1]} has a repeated row'); break
                    seen.add(key)
        elif r[0] == 'adjdistinct':
            v = A[r[1]]
            if isinstance(v, list) and any(a == b for a, b in zip(v, v[1:])): bad.append(f'{r[1]} has equal neighbours')
        elif r[0] == 'validtree':
            e = A[r[1]]
            n = A.get('n')
            if isinstance(e, list) and all(isinstance(x, list) and len(x) >= 2 for x in e):
                nodes = n if isinstance(n, int) else len({y for x in e for y in x[:2]}) if e else 1
                if len(e) != nodes - 1 or not _connected(nodes, e): bad.append(f'{r[1]} is not a valid tree')
        elif r[0] == 'unique':
            v = A[r[1]]
            if isinstance(v, list) and all(not isinstance(x, (list, dict)) for x in v) and len(set(v)) != len(v): bad.append(f'{r[1]} not unique')
        elif r[0] == 'sorted':
            v = A[r[1]]
            if isinstance(v, list) and all(isinstance(x, (int, float)) for x in v):
                dec = r[2] in ('non-increasing', 'descending')
                strict = r[2] == 'strictly increasing'
                ok = all((a >= b if dec else (a < b if strict else a <= b)) for a, b in zip(v, v[1:]))
                if not ok: bad.append(f'{r[1]} not sorted ({r[2]})')
    return bad

def audit_problem(folder):
    meta = engine.load_tests(folder); ref = engine.reference(folder)
    readme = open(os.path.join(engine.ROOT, 'problems', folder, 'README.md'), encoding='utf-8').read()
    kinds, _ = engine.param_kinds(ref['starter'], meta['method'])
    rules = parse(readme, meta['params'], folder)
    out = []
    for i, t in enumerate(meta['tests']):
        v = check(rules, meta['params'], t['a'], kinds)
        if v: out.append((i + 1, v))
    return rules, out

if __name__ == '__main__':
    import sys
    res = {}
    for d in sorted(os.listdir(os.path.join(engine.ROOT, 'problems'))):
        if os.path.exists(os.path.join(engine.ROOT, 'problems', d, 'tests.json')) and engine.reference(d):
            try: rules, v = audit_problem(d)
            except Exception as e: res[d] = {'error': repr(e)}; continue
            res[d] = {'rules': len(rules), 'violations': [{'i': i, 'why': w} for i, w in v]}
    os.makedirs('report', exist_ok=True)
    json.dump(res, open('report/constraints.json', 'w'), indent=0)
    tot = sum(len(r.get('violations', [])) for r in res.values())
    print('problems with violations:', sum(1 for r in res.values() if r.get('violations')), 'tests:', tot,
          'problems with 0 parsed rules:', sum(1 for r in res.values() if r.get('rules') == 0), 'errors:', sum(1 for r in res.values() if 'error' in r))
