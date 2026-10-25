"""Bookkeeping after tests.json files changed: audit counters, "unordered" hints, and the Tests column of INDEX.md."""
import json, os, re
import engine
from generate import ANY_ORDER

def main():
    counts = {}
    for d in sorted(os.listdir(os.path.join(engine.ROOT, 'problems'))):
        p = os.path.join(engine.ROOT, 'problems', d, 'tests.json')
        if not os.path.exists(p): continue
        m = json.load(open(p, encoding='utf-8'))
        readme = open(os.path.join(engine.ROOT, 'problems', d, 'README.md'), encoding='utf-8').read()
        a = m.setdefault('audit', {})
        a['added_generated'] = sum(1 for t in m['tests'] if t.get('g'))
        for k in [k for k, v in a.items() if v in (0, None)]: del a[k]
        if ANY_ORDER.search(readme): m['unordered'] = True      # statement allows any order: the UI defaults to order-insensitive comparison
        json.dump(m, open(p, 'w', encoding='utf-8'), separators=(',', ':'))
        counts[d] = len(m['tests'])
    idx = os.path.join(engine.ROOT, 'INDEX.md')
    out = []
    for line in open(idx, encoding='utf-8').read().split('\n'):
        c = [x.strip() for x in line.split('|')]
        if len(c) >= 7 and c[5] in counts:
            c[4] = str(counts[c[5]])
            line = '| ' + ' | '.join(c[1:6]) + ' |'
        out.append(line)
    open(idx, 'w', encoding='utf-8').write('\n'.join(out))
    print(sum(counts.values()), 'tests in', len(counts), 'problems')

if __name__ == '__main__': main()
