"""Hand-written generators for suites too thin to be perturbed from existing tests:
 - single-integer problems with a tiny input domain are covered exhaustively;
 - 1093 (256-entry count array) and 1583 (preference lists) get structured random inputs.
Expected values always come from the reference solution, cross-checked with the second solution."""
import json, os, random
import engine

def run(folder, args_list, tag):
    meta = engine.load_tests(folder); ref = engine.reference(folder)
    a = engine.Subject(folder, ref['completion'], meta); b = engine.Subject(folder, ref['response'], meta) if ref.get('response') else None
    have = {json.dumps(t['a']) for t in meta['tests']}
    n = 0
    for args in args_list:
        if json.dumps(args) in have: continue
        st, v = engine.run_case(a, args, 5)
        if st != 'ok': continue
        if b:
            st2, v2 = engine.run_case(b, args, 5)
            if st2 != 'ok' or not engine.eq(v, v2): continue
        meta['tests'].append({'a': args, 'e': v, 'g': tag}); have.add(json.dumps(args)); n += 1
    meta.setdefault('audit', {})['added_generated'] = meta.get('audit', {}).get('added_generated', 0) + n
    json.dump(meta, open(os.path.join(engine.ROOT, 'problems', folder, 'tests.json'), 'w'), separators=(',', ':'))
    print(folder, 'added', n, 'total', len(meta['tests']))

def main():
    for folder, lo, hi in [('0022-generate-parentheses', 1, 8), ('0357-count-numbers-with-unique-digits', 0, 8), 
                           ('0526-beautiful-arrangement', 1, 15), ('0096-unique-binary-search-trees', 1, 19)]:
        run(folder, [[i] for i in range(lo, hi + 1)], 'domain')
    rnd = random.Random(1093)
    cases = []
    for _ in range(60):   # sparse and dense samples; the mode must be unique (the problem guarantees it)
        cnt = [0] * 256
        k = rnd.choice([1, 2, 3, 5, 10, 50, 256])
        idx = rnd.sample(range(256), k)
        for i in idx: cnt[i] = rnd.randint(1, rnd.choice([3, 10, 100, 10**5]))
        top = max(cnt)
        if cnt.count(top) != 1: continue
        cases.append([cnt])
    cases.append([[0] * 255 + [1]]); cases.append([[1] + [0] * 255]); cases.append([[0] * 128 + [5] + [0] * 127])
    run('1093-statistics-from-a-large-sample', cases, 'gen')
    cases = []
    for n in [2, 4, 6, 8, 10, 12, 20, 50, 100]:
        for _ in range(4 if n < 20 else 1):
            prefs = []
            for i in range(n):
                others = [j for j in range(n) if j != i]; rnd.shuffle(others); prefs.append(others)
            perm = list(range(n)); rnd.shuffle(perm)
            pairs = [[perm[i], perm[i + 1]] for i in range(0, n, 2)]
            cases.append([n, prefs, pairs])
    run('1583-count-unhappy-friends', cases, 'gen')

if __name__ == '__main__': main()
