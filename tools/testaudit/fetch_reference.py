"""Builds reference.json.gz: independent Python reference solutions for every problem in problems/.

Source: newfacade/LeetCodeDataset (Apache-2.0), the same dataset the tests came from.
  `completion` = the dataset's reference solution, `response` = a second, independently written (LLM) solution.
Usage: python3 fetch_reference.py   (downloads ~100 MB to a temp dir, writes reference.json.gz next to this file)
"""
import gzip, json, os, re, sys, tempfile, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
BASE = 'https://huggingface.co/datasets/newfacade/LeetCodeDataset/resolve/main/LeetCodeDataset-%s.jsonl'

def main():
    slugs = {d.split('-', 1)[1]: d for d in os.listdir(os.path.join(ROOT, 'problems'))}
    out = {}
    tmp = tempfile.mkdtemp()
    for part in ('train', 'test'):
        path = os.path.join(tmp, part + '.jsonl')
        print('downloading', part, file=sys.stderr)
        urllib.request.urlretrieve(BASE % part, path)
        for line in open(path, encoding='utf-8'):
            r = json.loads(line)
            if r['task_id'] not in slugs: continue
            m = re.search(r'```python\n(.*?)```', r.get('response') or '', re.S)
            out[slugs[r['task_id']]] = {
                'prompt': r['prompt'], 'completion': r['completion'],
                'response': m.group(1) if m else None, 'starter': r['starter_code'],
            }
    with gzip.open(os.path.join(HERE, 'reference.json.gz'), 'wt', encoding='utf-8') as f:
        json.dump(out, f, separators=(',', ':'))
    print(len(out), 'problems', file=sys.stderr)

if __name__ == '__main__':
    main()
