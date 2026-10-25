"""How close do the tests get to the constraint limits? (A suite that never goes near n = 10^5 cannot catch O(n^2) code.)

For each README rule `lo <= X.length <= hi` (or a value range) it records the largest observed length/value and how far
that is from the limit. Prints distribution tables; `TESTS_ROOT=<dir>` audits another copy of the tests."""
import json, math, os, sys
import constraints, engine

def analyse(root_problems=None):
    rows = []
    for d in sorted(os.listdir(os.path.join(engine.ROOT, 'problems'))):
        if not os.path.exists(os.path.join(engine.ROOT, 'problems', d, 'tests.json')) or not engine.reference(d): continue
        meta = engine.load_tests(d); ref = engine.reference(d)
        readme = open(os.path.join(engine.ROOT, 'problems', d, 'README.md'), encoding='utf-8').read()
        kinds, _ = engine.param_kinds(ref['starter'], meta['method'])
        try: rules = constraints.parse(readme, meta['params'], d)
        except Exception: continue
        K = dict(zip(meta['params'], kinds))
        best = None   # (hi, observed max) for the largest length-bound rule
        for r in rules:
            if r[0] != 'chain': continue
            _, terms, ops = r
            if len(terms) != 3 or terms[0][0] != 'lit' or terms[2][0] != 'lit' or terms[1][0] != 'acc': continue
            acc = terms[1]
            if not acc[3] or acc[2] != 0: continue            # only X.length of a top-level list/string
            hi = max(constraints.bound_values(terms[2][1]))
            obs = 0
            for t in meta['tests']:
                v = dict(zip(meta['params'], t['a'])).get(acc[1])
                if isinstance(v, (list, str)): obs = max(obs, len(v))
            if best is None or hi > best[0]: best = (hi, obs)
        if best: rows.append((d, best[0], best[1], len(meta['tests'])))
    return rows

def table(rows):
    big = [r for r in rows if r[1] >= 10**4]
    def pct(x, n): return f'{x} ({100*x//max(n,1)}%)'
    n = len(big)
    print(f'problems with a length limit >= 10^4: {n}')
    print('  tests reach >= 1,000 elements :', pct(sum(1 for r in big if r[2] >= 1000), n))
    print('  tests reach >= 10% of the limit:', pct(sum(1 for r in big if r[2] >= r[1] / 10), n))
    print('  tests reach the limit          :', pct(sum(1 for r in big if r[2] >= r[1]), n))
    print('  largest test < 100 elements    :', pct(sum(1 for r in big if r[2] < 100), n))

if __name__ == '__main__':
    table(analyse())
