"""0236 Lowest Common Ancestor: the dataset's tests had no usable expected values (p, q are node references).
Rebuild them: p and q are node values (the C# runner resolves them inside the tree), `e` is the value of the LCA."""
import json, os, random
import engine

def build(vals):
    if not vals or vals[0] is None: return None
    nodes = [[vals[0], None, None]]; q = [nodes[0]]; i = 1; k = 0
    while k < len(q) and i < len(vals):
        n = q[k]; k += 1
        for side in (1, 2):
            if i < len(vals):
                if vals[i] is not None: c = [vals[i], None, None]; n[side] = c; q.append(c)
                i += 1
    return nodes[0]

def lca(root, p, q):
    if root is None or root[0] in (p, q): return root
    l, r = lca(root[1], p, q), lca(root[2], p, q)
    return root if l and r else (l or r)

def values(root):
    out, st = [], [root]
    while st:
        n = st.pop()
        if n: out.append(n[0]); st += [n[1], n[2]]
    return out

def serialize(n):
    out, q, k = [], [n], 0
    while k < len(q):
        x = q[k]; k += 1
        if x is None: out.append(None); continue
        out.append(x[0]); q += [x[1], x[2]]
    while out and out[-1] is None: out.pop()
    return out

def random_tree(rnd, n, skew=False):
    vals = rnd.sample(range(-10**9 // 1000, 10**9 // 1000), n)
    root = [vals[0], None, None]; nodes = [root]
    for v in vals[1:]:
        while True:
            par = nodes[-1] if skew and rnd.random() < .9 else rnd.choice(nodes)
            side = rnd.choice([1, 2])
            if par[side] is None: c = [v, None, None]; par[side] = c; nodes.append(c); break
    return root

def main():
    d = '0236-lowest-common-ancestor-of-a-binary-tree'
    path = os.path.join(engine.ROOT, 'problems', d, 'tests.json')
    meta = json.load(open(path))
    tests, seen = [], set()
    def add(tree_list, p, q, tag=None):
        root = build(tree_list); vs = values(root)
        if len(set(vs)) != len(vs) or p == q or p not in vs or q not in vs or not (1 <= len(vs) <= 10**5): return
        key = json.dumps([tree_list, p, q])
        if key in seen: return
        seen.add(key)
        t = {'a': [tree_list, p, q], 'e': lca(root, p, q)[0]}
        if tag: t['g'] = tag
        tests.append(t)
    for t in meta['tests']: add(*t['a'])
    rnd = random.Random(236)
    add([1, 2], 1, 2); add([1, 2], 2, 1); add([1, None, 2], 1, 2); add([-1, 0], 0, -1)
    for n in (3, 5, 8, 15, 30, 60, 100, 300):
        for _ in range(6):
            r = random_tree(rnd, n); vs = values(r); p, q = rnd.sample(vs, 2)
            add(serialize(r), p, q, 'gen')
    for n in (2000, 10000):
        r = random_tree(rnd, n, skew=True); vs = values(r); p, q = rnd.sample(vs, 2); add(serialize(r), p, q, 'perf')
    meta['tests'] = tests; meta['audit'] = {'rebuilt': 'p and q are node values; e is the LCA value'}
    json.dump(meta, open(path, 'w'), separators=(',', ':'))
    print(len(tests), 'tests')

if __name__ == '__main__': main()
