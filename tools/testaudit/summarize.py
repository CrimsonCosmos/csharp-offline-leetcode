import json, sys
def stats(path):
    R = [r for r in json.load(open(path)) if 'error' not in r]
    M = sum(r['mutants'] for r in R); K = sum(r['killed'] for r in R)
    return dict(problems=len(R), tests=sum(r['tests'] for r in R), mutants=M, killed=K, score=round(K / M, 4),
                perfect=sum(1 for r in R if r['mutants'] and r['killed'] == r['mutants']),
                low=sum(1 for r in R if r['mutants'] >= 5 and r['killed'] / r['mutants'] < .9),
                ref_mismatch=sum(r['ref_mismatch_n'] for r in R), second_mismatch_problems=sum(1 for r in R if r.get('second_mismatch_n')))
for p in sys.argv[1:]: print(p, stats(p))
