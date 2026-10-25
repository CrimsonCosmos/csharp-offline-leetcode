"""Remove test cases that cannot occur on LeetCode: inputs violating the README constraints, and exact duplicates.

  python3 clean_tests.py            # dry run, prints a summary
  python3 clean_tests.py --apply    # rewrites problems/*/tests.json, logs removals to report/removed_tests.json.gz

Idempotent. Each tests.json gets an "audit" object recording what was removed.
"""
import gzip, json, os, sys
import constraints, engine

def main(apply):
    removed_log, stats = {}, []
    for d in sorted(os.listdir(os.path.join(engine.ROOT, 'problems'))):
        path = os.path.join(engine.ROOT, 'problems', d, 'tests.json')
        if not os.path.exists(path) or not engine.reference(d): continue
        meta = engine.load_tests(d)
        try: rules, viol = constraints.audit_problem(d)
        except Exception as e:
            print('skip', d, repr(e), file=sys.stderr); continue
        bad = {i: w for i, w in viol}
        keep, seen, gone = [], set(), []
        for i, t in enumerate(meta['tests'], 1):
            key = json.dumps(t['a'], sort_keys=True)
            if i in bad: gone.append({'i': i, 'why': 'constraint: ' + '; '.join(bad[i])[:200], 'test': t})
            elif key in seen: gone.append({'i': i, 'why': 'duplicate input', 'test': t})
            else: seen.add(key); keep.append(t)
        if not gone: continue
        stats.append((d, len(meta['tests']), len(gone)))
        removed_log[d] = gone
        if apply:
            a = meta.setdefault('audit', {})
            a['removed_invalid'] = a.get('removed_invalid', 0) + sum(1 for g in gone if g['why'].startswith('constraint'))
            a['removed_duplicates'] = a.get('removed_duplicates', 0) + sum(1 for g in gone if g['why'].startswith('duplicate'))
            meta['tests'] = keep
            with open(path, 'w', encoding='utf-8') as f: json.dump(meta, f, separators=(',', ':'))
    tot_before = sum(s[1] for s in stats); tot_gone = sum(s[2] for s in stats)
    print(f'{len(stats)} problems affected, {tot_gone} tests removed ({tot_gone} of {tot_before} in those problems)')
    low = sorted([(s[1] - s[2], s[0]) for s in stats if s[1] - s[2] < 20])
    print('problems left with < 20 tests:', len(low), low[:15])
    if apply:
        os.makedirs(os.path.join(engine.HERE, 'report'), exist_ok=True)
        with gzip.open(os.path.join(engine.HERE, 'report', 'removed_tests.json.gz'), 'wt', encoding='utf-8') as f: json.dump(removed_log, f)

if __name__ == '__main__':
    main('--apply' in sys.argv)
