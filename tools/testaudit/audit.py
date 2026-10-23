"""Audit the quality of problems/*/tests.json using independent Python reference solutions.

  python3 audit.py [--jobs 4] [--mutants 60] [folder-substring ...]

For every problem it
  1. runs the reference solution (dataset `completion`) and a second independent solution (`response`)
     on every test and counts disagreements with the expected values (cross-validation of the test data);
  2. mutation-tests the suite: seeded mutants of the reference solution (flipped comparisons, off-by-one constants,
     swapped operators, negated conditions ...) are run against the tests; a mutant that passes every test
     SURVIVED, which points to behaviour the suite never exercises (or to an equivalent mutant).
Writes report/audit.json (+ report/SUMMARY.md). Deterministic: fixed seeds, no network.
"""
import json, os, resource, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
import engine

REPORT = os.path.join(engine.HERE, 'report')

def kills(subject, tests, expected, limit):
    for i, t in enumerate(tests):
        st, v = engine.run_case(subject, t['a'], limit)
        if st != 'ok' or not engine.eq(v, expected[i]): return True
    return False

def worker(folder, nmut, family='A', seed_off=0):
    resource.setrlimit(resource.RLIMIT_AS, (3 << 30, 3 << 30))
    meta = engine.load_tests(folder); ref = engine.reference(folder); tests = meta['tests']
    res = {'folder': folder, 'tests': len(tests), 'inplace': meta['inplace']}
    keys = [json.dumps(t['a'], sort_keys=True) for t in tests]
    res['duplicates'] = len(keys) - len(set(keys))
    subj = engine.Subject(folder, ref['completion'], meta)
    expected, mism, slow = [], [], 0.0
    for i, t in enumerate(tests):
        t0 = time.time(); st, v = engine.run_case(subj, t['a'], 5); slow = max(slow, time.time() - t0)
        e = v if meta['inplace'] else engine.canon_expected(subj.ns, t['e'], subj.rkind)
        expected.append(e)
        if not meta['inplace'] and not (st == 'ok' and engine.eq(v, e)): mism.append(i + 1)
    res['ref_mismatch'] = mism[:20]; res['ref_mismatch_n'] = len(mism)
    # second solution
    if ref.get('response'):
        try:
            s2 = engine.Subject(folder, ref['response'], meta); bad = 0
            for i, t in enumerate(tests):
                st, v = engine.run_case(s2, t['a'], 5)
                if not (st == 'ok' and engine.eq(v, expected[i])): bad += 1
            res['second_mismatch_n'] = bad
        except Exception as e:
            res['second_error'] = type(e).__name__
    # mutation testing
    limit = max(0.5, min(3.0, slow * 20 + 0.3))
    muts, total = engine.make_mutants(ref['completion'], nmut, seed=hash_seed(folder) + seed_off, family=family)
    res['mutation_sites'] = total
    killed, survivors = 0, []
    for src, desc in muts:
        try: ms = engine.Subject(folder, src, meta)
        except Exception: continue
        if kills(ms, tests, expected, limit): killed += 1
        else: survivors.append(desc)
    res['mutants'] = killed + len(survivors); res['killed'] = killed; res['survivors'] = survivors
    return res

def hash_seed(s):
    h = 17
    for c in s: h = (h * 31 + ord(c)) % 1000003
    return h

def run_one(args):
    folder, nmut, family, seed_off = args
    t0 = time.time()
    try:
        p = subprocess.run(['bash', '-c', 'ulimit -s 1000000; exec python3 "$0" --worker "$1" "$2" "$3" "$4"', sys.argv[0], folder, str(nmut), family, str(seed_off)],
                           capture_output=True, text=True, timeout=600, cwd=engine.HERE)
        line = [l for l in p.stdout.splitlines() if l.startswith('{')]
        r = json.loads(line[-1]) if line else {'folder': folder, 'error': (p.stderr or p.stdout)[-400:]}
    except subprocess.TimeoutExpired:
        r = {'folder': folder, 'error': 'audit timeout'}
    r['secs'] = round(time.time() - t0, 1)
    return r

def main():
    argv = sys.argv[1:]
    if argv and argv[0] == '--worker':
        print(json.dumps(worker(argv[1], int(argv[2]), argv[3], int(argv[4])))); return
    jobs, nmut, filt, family, seed_off, outname = 4, 60, [], 'A', 0, 'audit'
    i = 0
    while i < len(argv):
        if argv[i] == '--jobs': jobs = int(argv[i + 1]); i += 2
        elif argv[i] == '--mutants': nmut = int(argv[i + 1]); i += 2
        elif argv[i] == '--family': family = argv[i + 1]; i += 2
        elif argv[i] == '--seed-offset': seed_off = int(argv[i + 1]); i += 2
        elif argv[i] == '--out': outname = argv[i + 1]; i += 2
        else: filt.append(argv[i]); i += 1
    folders = sorted(d for d in os.listdir(os.path.join(engine.ROOT, 'problems'))
                     if os.path.exists(os.path.join(engine.ROOT, 'problems', d, 'tests.json')) and engine.reference(d)
                     and (not filt or any(f in d for f in filt)))
    os.makedirs(REPORT, exist_ok=True)
    out, done = [], 0
    with ThreadPoolExecutor(jobs) as ex:
        for r in ex.map(run_one, [(f, nmut, family, seed_off) for f in folders]):
            out.append(r); done += 1
            if done % 25 == 0: print(f'{done}/{len(folders)}', file=sys.stderr, flush=True)
    path = os.path.join(REPORT, outname + ('.json' if not filt else '_partial.json'))
    json.dump(out, open(path, 'w'), indent=0)
    print('wrote', path, file=sys.stderr)

if __name__ == '__main__':
    main()
