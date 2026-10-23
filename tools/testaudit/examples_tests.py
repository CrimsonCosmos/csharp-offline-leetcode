"""Problems the dataset has no tests for (154): build tests from the examples in the README.

 - ordinary problems: `Input: a = [1,2], b = 3` / `Output: 4` pairs;
 - design problems (class with a constructor and several methods): the LeetCode "Input / Output" operation sequences,
   run by the runner's design mode ("design": true).
These suites are tagged "examplesOnly": a pass is a smoke test, not evidence of correctness.
Problems whose outputs are random, interactive, or use unsupported types are skipped.
"""
import json, os, re, sys
import engine
from generate import csharp_sig, ANY_ORDER

SKIP_NAME = re.compile(r'random|shuffle|rand7|rand10', re.I)

def jload(s):
    s = s.strip()
    try: return True, json.loads(s)
    except Exception: return False, None

def split_input(inp, names):
    """'nums = [1,2], target = 3' -> [[1,2], 3] (None if it cannot be parsed)."""
    pos = []
    for n in names:
        m = re.search(r'(?:(?<=^)|(?<=[\s,]))' + re.escape(n) + r'\s*=\s*', inp)
        if not m: return None
        pos.append((m.start(), m.end(), n))
    pos.sort()
    if [p[2] for p in pos] != names: return None
    vals = []
    for i, (s, e, n) in enumerate(pos):
        end = pos[i + 1][0] if i + 1 < len(pos) else len(inp)
        ok, v = jload(inp[e:end].strip().rstrip(','))
        if not ok: return None
        vals.append(v)
    return vals

def examples(readme):
    out = []
    for m in re.finditer(r'```\n(.*?)```', readme, re.S):
        out.append(m.group(1))
    return out

def make_simple(folder, readme, sol):
    sig = csharp_sig(folder)
    m = re.search(r'public\s+[\w<>\[\],\s\?]+?\s+(\w+)\s*\(([^)]*)\)\s*\{', sol)
    if not sig or not m: return None
    names = []
    depth = 0; cur = ''
    for ch in m.group(2) + ',':
        if ch == '<': depth += 1
        if ch == '>': depth -= 1
        if ch == ',' and depth == 0:
            if cur.strip(): names.append(cur.strip().rsplit(' ', 1)[1])
            cur = ''
        else: cur += ch
    tests = []
    for blk in examples(readme):
        mm = re.match(r'Input: (.*?)\nOutput: (.*?)(?:\nExplanation:.*)?\s*$', blk, re.S)
        if not mm: continue
        a = split_input(mm.group(1).strip(), names)
        ok, e = jload(mm.group(2))
        if a is None or not ok: continue
        tests.append({'a': a, 'e': e, 'g': 'example'})
    if not tests: return None
    meta = {'slug': folder.split('-', 1)[1], 'method': m.group(1), 'params': names, 'inplace': False, 'tests': tests,
            'examplesOnly': True}
    return meta

def make_design(folder, readme, sol):
    cm = re.search(r'public class (\w+)', sol)
    if not cm: return None
    cls = cm.group(1)
    if SKIP_NAME.search(folder) or SKIP_NAME.search(cls): return None
    tests = []
    for blk in examples(readme):
        mm = re.match(r'Input:?\s*\n(\[.*?\])\s*\n(\[.*?\])\s*\nOutput:?\s*\n(\[.*?\])\s*(?:\nExplanation.*)?$', blk, re.S)
        if not mm: continue
        o1, o2, o3 = jload(mm.group(1)), jload(mm.group(2)), jload(mm.group(3))
        if not (o1[0] and o2[0] and o3[0]): continue
        ops, args, exp = o1[1], o2[1], o3[1]
        if not (len(ops) == len(args) == len(exp)) or ops[0] != cls: continue
        tests.append({'ops': ops, 'a': args, 'e': exp, 'g': 'example'})
    if not tests: return None
    return {'slug': folder.split('-', 1)[1], 'design': True, 'class': cls, 'inplace': False, 'method': '', 'params': [], 'tests': tests, 'examplesOnly': True}

def main():
    made = {'simple': 0, 'design': 0}; skipped = []
    for d in sorted(os.listdir(os.path.join(engine.ROOT, 'problems'))):
        base = os.path.join(engine.ROOT, 'problems', d)
        if os.path.exists(os.path.join(base, 'tests.json')): continue
        sol = open(os.path.join(base, 'Solution.cs'), encoding='utf-8').read()
        readme = open(os.path.join(base, 'README.md'), encoding='utf-8').read()
        design = 'class Solution' not in sol
        meta = make_design(d, readme, sol) if design else make_simple(d, readme, sol)
        if not meta: skipped.append(d); continue
        if ANY_ORDER.search(readme): meta['unordered'] = True
        meta['audit'] = {'source': 'README examples'}
        json.dump(meta, open(os.path.join(base, 'tests.json'), 'w'), separators=(',', ':'))
        made['design' if design else 'simple'] += 1
    print(made, 'skipped', len(skipped)); print(skipped)

if __name__ == '__main__': main()
