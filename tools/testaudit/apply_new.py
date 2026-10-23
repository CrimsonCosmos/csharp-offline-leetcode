"""Merge report/new/<folder>.json (written by generate.py) into problems/<folder>/tests.json. Idempotent."""
import json, os, sys
import engine

def main():
    nd = os.path.join(engine.HERE, 'report', 'new')
    added = files = 0
    for fn in sorted(os.listdir(nd)):
        folder = fn[:-5]
        new = json.load(open(os.path.join(nd, fn)))
        if not new: continue
        path = os.path.join(engine.ROOT, 'problems', folder, 'tests.json')
        meta = json.load(open(path, encoding='utf-8'))
        have = {json.dumps(t['a'], sort_keys=True) for t in meta['tests']}
        fresh = [t for t in new if json.dumps(t['a'], sort_keys=True) not in have]
        if not fresh: continue
        if os.environ.get('REPLACE_PERF'): meta['tests'] = [t for t in meta['tests'] if t.get('g') != 'perf']; have = {json.dumps(t['a'], sort_keys=True) for t in meta['tests']}
        meta['tests'].extend(fresh)
        a = meta.setdefault('audit', {})
        a['added_generated'] = a.get('added_generated', 0) + len(fresh)
        with open(path, 'w', encoding='utf-8') as f: json.dump(meta, f, separators=(',', ':'))
        added += len(fresh); files += 1
    print(f'added {added} tests to {files} problems')

if __name__ == '__main__':
    main()
