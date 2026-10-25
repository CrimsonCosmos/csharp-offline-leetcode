"""Check that every test in every tests.json can be deserialized by the C# runner into the method's real C# types
(int overflow, a decimal inside a tree, unsupported types ... make the runner skip a test silently).

  python3 check_csharp.py [--jobs 3] [folder-substring ...]      -> report/csharp_check.json
Needs the .NET SDK. Compiles each problem's stub with a throwing body, then runs the runner with --check --json.
"""
import json, os, re, shutil, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor
import engine

PROJ = '''<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><OutputType>Exe</OutputType><TargetFramework>net8.0</TargetFramework><RollForward>Major</RollForward>
<ImplicitUsings>enable</ImplicitUsings><Nullable>disable</Nullable><EnableDefaultCompileItems>false</EnableDefaultCompileItems><InvariantGlobalization>true</InvariantGlobalization>
<NoWarn>CS8632;CS0168;CS0219;CS8981;CS0162;CS0649</NoWarn></PropertyGroup><ItemGroup><Compile Include="{p}/Program.cs" /><Compile Include="{p}/Helpers.cs" /><Compile Include="All.cs" /></ItemGroup></Project>'''

def stub(folder):
    src = open(os.path.join(engine.ROOT, 'problems', folder, 'Solution.cs'), encoding='utf-8').read()
    return re.sub(r'\{\s*\}', '{ throw new System.NotImplementedException(); }', src)

def build_all(folders, work):
    """One assembly with every stub in its own namespace (P0001, ...); returns the folders that compiled."""
    good = list(folders)
    for attempt in range(6):
        parts = [f'namespace P{f.split("-")[0]} {{\n{stub(f)}\n}}\n' for f in good]
        open(os.path.join(work, 'All.cs'), 'w').write('\n'.join(parts))
        open(os.path.join(work, 'c.csproj'), 'w').write(PROJ.format(p=os.path.join(engine.ROOT, 'Practice')).replace('Solution.cs', 'All.cs'))
        b = subprocess.run(['dotnet', 'build', '-c', 'Release', '--nologo', '-v', 'q', '-clp:NoSummary'], cwd=work, capture_output=True, text=True, timeout=900)
        if b.returncode == 0: return good, []
        # drop the namespaces that contain errors and retry
        lines = open(os.path.join(work, 'All.cs')).read().split('\n')
        bad_lines = {int(m.group(1)) for m in re.finditer(r'All\.cs\((\d+),', b.stdout + b.stderr)}
        if not bad_lines: raise RuntimeError((b.stdout + b.stderr)[-1500:])
        ns_of = {}
        cur = None
        for i, l in enumerate(lines, 1):
            m = re.match(r'namespace P(\d+) \{', l)
            if m: cur = m.group(1)
            ns_of[i] = cur
        bad = {ns_of[l] for l in bad_lines if l in ns_of}
        dropped = [f for f in good if f.split('-')[0] in bad]
        good = [f for f in good if f.split('-')[0] not in bad]
        if not dropped: raise RuntimeError((b.stdout + b.stderr)[-1500:])
        print('stubs that do not compile:', dropped, file=sys.stderr)
    raise RuntimeError('too many rounds')

def check_one(args):
    folder, work = args
    r = subprocess.run(['dotnet', 'exec', os.path.join(work, 'bin', 'Release', 'net8.0', 'c.dll'), os.path.join(engine.ROOT, 'problems', folder),
                        '--json', '--check', '--ns=P' + folder.split('-')[0]], cwd=work, capture_output=True, text=True, timeout=300)
    line = [l for l in r.stdout.splitlines() if l.startswith('{')]
    if not line: return {'folder': folder, 'error': 'run: ' + (r.stdout + r.stderr)[-300:]}
    j = json.loads(line[-1])
    return {'folder': folder, 'passed': j.get('passed'), 'total': j.get('total'), 'skipped': j.get('skipped', 0), 'skippedIdx': j.get('skippedIdx', []), 'message': j.get('message', '')[-200:], 'code': j.get('code')}

def main():
    argv = sys.argv[1:]; jobs = 3; filt = []; apply = '--apply' in argv; argv = [a for a in argv if a != '--apply']
    i = 0
    while i < len(argv):
        if argv[i] == '--jobs': jobs = int(argv[i + 1]); i += 2
        else: filt.append(argv[i]); i += 1
    folders = sorted(d for d in os.listdir(os.path.join(engine.ROOT, 'problems'))
                     if os.path.exists(os.path.join(engine.ROOT, 'problems', d, 'tests.json')) and (not filt or any(f in d for f in filt)))
    work = tempfile.mkdtemp(prefix='cschk_')
    try:
        good, _ = build_all(folders, work)
        out = [{'folder': f, 'error': 'stub does not compile'} for f in folders if f not in good]
        with ThreadPoolExecutor(jobs) as ex:
            for n, r in enumerate(ex.map(check_one, [(f, work) for f in good]), 1):
                out.append(r)
                if n % 100 == 0: print(f'{n}/{len(good)}', file=sys.stderr, flush=True)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    path = os.path.join(engine.HERE, 'report', 'csharp_check.json' if not filt else 'csharp_check_partial.json')
    json.dump(out, open(path, 'w'), indent=0)
    bad = [r for r in out if 'error' in r or r.get('skipped') or r.get('code') not in (0, None)]
    if apply:   # drop tests the runner would silently skip (value does not fit the C# type, e.g. an answer beyond int range)
        import gzip
        lp = os.path.join(engine.HERE, 'report', 'removed_untypeable.json.gz')
        log = json.load(gzip.open(lp, 'rt')) if os.path.exists(lp) else {}
        for r in out:
            if r.get('skippedIdx'):
                p = os.path.join(engine.ROOT, 'problems', r['folder'], 'tests.json')
                m = json.load(open(p, encoding='utf-8')); drop = set(r['skippedIdx'])
                log.setdefault(r['folder'], []).extend(t for i, t in enumerate(m['tests'], 1) if i in drop)
                m['tests'] = [t for i, t in enumerate(m['tests'], 1) if i not in drop]
                m.setdefault('audit', {})['removed_untypeable'] = len(drop)
                json.dump(m, open(p, 'w', encoding='utf-8'), separators=(',', ':'))
        with gzip.open(lp, 'wt') as f: json.dump(log, f)
        print('removed', sum(len(v) for v in log.values()), 'untypeable tests from', len(log), 'problems')
    print(len(out), 'problems checked;', len(bad), 'with a problem:')
    for r in bad[:40]: print(' ', r['folder'], r.get('error') or f"skipped {r.get('skipped')}/{r.get('total')} {r.get('message','')[:80]}")

if __name__ == '__main__': main()
