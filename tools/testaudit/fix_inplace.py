"""Give the in-place problems real expectations: run the reference solution and store the final state of the mutated
argument as `e`, plus "inplaceArg" (index of that argument) in tests.json so the C# runner can verify it."""
import copy, json, os
import engine

def main():
    for d in sorted(os.listdir(os.path.join(engine.ROOT, 'problems'))):
        p = os.path.join(engine.ROOT, 'problems', d, 'tests.json')
        if not os.path.exists(p) or not engine.reference(d): continue
        meta = engine.load_tests(d)
        if not meta['inplace']: continue
        ref = engine.reference(d); subj = engine.Subject(d, ref['completion'], meta)
        sec = engine.Subject(d, ref['response'], meta) if ref.get('response') else None
        changed = set(); results = []
        for t in meta['tests']:
            st, v = engine.run_case(subj, t['a'], 10)    # v = normalized list of all (python) args after the call
            assert st == 'ok', (d, st, v)
            results.append(v)
            for i, (before, after) in enumerate(zip(t['a'], v)):
                if engine.normalize(engine.canon_expected(subj.ns, before, subj.kinds[i])) != after: changed.add(i)
        assert len(changed) == 1, (d, changed)
        idx = changed.pop(); agree = 0
        for t, v in zip(meta['tests'], results):
            t['e'] = v[idx]
            if sec:
                st, v2 = engine.run_case(sec, t['a'], 10)
                agree += st == 'ok' and engine.eq(v2[idx], v[idx])
        meta['inplaceArg'] = idx
        meta.setdefault('audit', {})['inplace_verified'] = True
        json.dump(meta, open(p, 'w'), separators=(',', ':'))
        print(f'{d}: arg {idx} ({meta["params"][idx]}), second solution agrees on {agree}/{len(meta["tests"])}')

if __name__ == '__main__':
    main()
