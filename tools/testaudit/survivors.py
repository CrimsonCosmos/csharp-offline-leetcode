"""Show the surviving mutants of a problem as diffs (for judging equivalent mutants vs. missing tests)."""
import ast, difflib, json, sys
import engine
from generate import hash_seed

def main(folder, extra=None):
    meta = engine.load_tests(folder); ref = engine.reference(folder)
    tests = meta['tests'] + (extra or [])
    subj = engine.Subject(folder, ref['completion'], meta)
    exp = []
    for t in tests:
        st, v = engine.run_case(subj, t['a'], 5); exp.append(v)
    base = ast.unparse(ast.parse(ref['completion'])).splitlines()
    muts, _ = engine.make_mutants(ref['completion'], 150, seed=7919 + len(folder))
    for src, desc in muts:
        try: ms = engine.Subject(folder, src, meta)
        except Exception: continue
        if all((lambda r: r[0] == 'ok' and engine.eq(r[1], e))(engine.run_case(ms, t['a'], 2)) for t, e in zip(tests, exp)):
            d = [l for l in difflib.unified_diff(base, src.splitlines(), lineterm='', n=0) if not l.startswith(('---', '+++', '@@'))]
            print(desc, ' | '.join(l.strip() for l in d))

if __name__ == '__main__':
    main(sys.argv[1])
