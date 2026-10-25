"""Shared pieces: load a problem + its Python reference, run test cases, compare like the C# runner, mutate code."""
import ast, copy, gzip, json, math, os, random, re, signal, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.setrecursionlimit(20000)

_REF = None
def reference(folder):
    global _REF
    if _REF is None:
        with gzip.open(os.path.join(HERE, 'reference.json.gz'), 'rt', encoding='utf-8') as f:
            _REF = json.load(f)
    return _REF.get(folder)

def load_tests(folder):
    base = os.environ.get('TESTS_ROOT') or os.path.join(ROOT, 'problems')   # TESTS_ROOT: audit another copy of the tests
    with open(os.path.join(base, folder, 'tests.json'), encoding='utf-8') as f:
        return json.load(f)

# ---------------------------------------------------------------- environment for a solution
class Timeout(Exception): pass

def _alarm(sig, frm): raise Timeout()

def with_timeout(seconds, fn, *a):
    signal.signal(signal.SIGALRM, _alarm)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try: return fn(*a)
    finally: signal.setitimer(signal.ITIMER_REAL, 0)

def make_namespace(prompt):
    ns = {'__name__': 'sol'}
    exec(compile(prompt, 'prompt', 'exec'), ns)   # imports, ListNode, TreeNode, helpers
    return ns

def build_solution(prompt, code, method):
    ns = make_namespace(prompt)
    exec(compile(code, 'solution', 'exec'), ns)
    return ns, ns['Solution']

def param_kinds(starter, method):
    """'list' / 'tree' / 'lists' / 'trees' / None for each parameter, plus the return kind."""
    tree = ast.parse(starter.rstrip() + '\n        pass\n')
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == method:
            def kind(a):
                if a is None: return None
                s = ast.unparse(a)
                if 'ListNode' in s: return 'lists' if s.startswith(('List[', 'list[')) else 'list'
                if 'TreeNode' in s: return 'trees' if s.startswith(('List[', 'list[')) else 'tree'
                return None
            return [kind(a.annotation) for a in node.args.args[1:]], kind(node.returns)
    raise KeyError(method)

def to_python_args(ns, args, kinds):
    out = []
    for a, k in zip(args, kinds):
        a = copy.deepcopy(a)
        if k == 'list': a = ns['list_node'](a)
        elif k == 'tree': a = ns['tree_node'](a)
        elif k == 'lists': a = [ns['list_node'](x) for x in a]
        elif k == 'trees': a = [ns['tree_node'](x) for x in a]
        out.append(a)
    return out

def node_to_list(n):
    if n is None: return []
    if hasattr(n, 'next'):
        out, seen = [], 0
        while n is not None:
            out.append(n.val); n = n.next; seen += 1
            if seen > 100000: raise ValueError('cycle')
        return out
    out, q = [], [n]
    i = 0
    while i < len(q):
        x = q[i]; i += 1
        if x is None: out.append(None); continue
        out.append(x.val); q.append(x.left); q.append(x.right)
    while out and out[-1] is None: out.pop()
    return out

def normalize(v):
    if hasattr(v, 'val') and (hasattr(v, 'next') or hasattr(v, 'left')): return node_to_list(v)
    if isinstance(v, (list, tuple)): return [normalize(x) for x in v]
    if isinstance(v, dict): return {str(k): normalize(x) for k, x in v.items()}
    if isinstance(v, (set, frozenset)): return sorted(normalize(x) for x in v)
    return v

def canon_expected(ns, e, rkind):
    """Expected value from tests.json in the same normalized form as normalize(result)."""
    if rkind == 'list': return node_to_list(ns['list_node'](e)) if e else []
    if rkind == 'tree': return node_to_list(ns['tree_node'](e)) if e else []
    return e

def eq(a, b):
    """Same rules as Program.Eq in the C# runner (numbers: exact unless either has a fraction, then 1e-5 relative)."""
    if isinstance(a, bool) or isinstance(b, bool): return a is b or (isinstance(a, bool) and isinstance(b, bool) and a == b)
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if isinstance(a, int) and isinstance(b, int): return a == b
        if math.isnan(a) and math.isnan(b): return True
        if a == b: return True
        if math.isinf(a) or math.isinf(b): return False
        return abs(a - b) <= 1e-5 * max(1.0, abs(b))
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        return len(a) == len(b) and all(eq(x, y) for x, y in zip(a, b))
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(eq(a[k], b[k]) for k in a)
    return a == b

class Subject:
    """A callable solution wrapped with argument/result conversion."""
    def __init__(self, folder, code, meta):
        ref = reference(folder)
        self.ns, self.cls = build_solution(ref['prompt'], code, meta['method'])
        self.method = meta['method']
        self.kinds, self.rkind = param_kinds(ref['starter'], self.method)
        self.inplace = meta['inplace']

    def call(self, args):
        obj = self.cls()
        pa = to_python_args(self.ns, args, self.kinds)
        fn = getattr(obj, self.method)
        r = fn(*pa)
        if r is None and self.rkind in ('list', 'tree'): return []   # empty list / empty tree
        if r is None and self.inplace:
            # in-place problem: the observable result is the state of the (first modified) argument
            return normalize(pa)
        return normalize(r)

def run_case(subject, args, limit):
    """-> ('ok', value) | ('err', repr) | ('timeout', None)"""
    try:
        return 'ok', with_timeout(limit, subject.call, args)
    except Timeout:
        return 'timeout', None
    except RecursionError:
        return 'err', 'RecursionError'
    except MemoryError:
        return 'err', 'MemoryError'
    except Exception as e:
        return 'err', type(e).__name__

# ---------------------------------------------------------------- mutation
CMP = {ast.Lt: [ast.LtE], ast.LtE: [ast.Lt], ast.Gt: [ast.GtE], ast.GtE: [ast.Gt], ast.Eq: [ast.NotEq], ast.NotEq: [ast.Eq]}
BIN = {ast.Add: [ast.Sub], ast.Sub: [ast.Add], ast.Mult: [ast.Add], ast.FloorDiv: [ast.Mult], ast.Mod: [ast.FloorDiv],
       ast.BitAnd: [ast.BitOr], ast.BitOr: [ast.BitAnd], ast.BitXor: [ast.BitOr], ast.LShift: [ast.RShift], ast.RShift: [ast.LShift]}

class Site:
    def __init__(self, kind, node, alt, line): self.kind, self.node, self.alt, self.line = kind, node, alt, line

def find_sites(tree):
    sites = []
    for node in ast.walk(tree):
        line = getattr(node, 'lineno', 0)
        if isinstance(node, ast.Compare):
            for i, op in enumerate(node.ops):
                for alt in CMP.get(type(op), []): sites.append(Site('cmp', (node, i), alt, line))
        elif isinstance(node, ast.BinOp):
            for alt in BIN.get(type(node.op), []): sites.append(Site('bin', node, alt, line))
        elif isinstance(node, ast.AugAssign):
            for alt in BIN.get(type(node.op), []): sites.append(Site('aug', node, alt, line))
        elif isinstance(node, ast.BoolOp):
            sites.append(Site('bool', node, ast.Or if isinstance(node.op, ast.And) else ast.And, line))
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            sites.append(Site('not', node, None, line))
        elif isinstance(node, ast.Constant) and type(node.value) is int:
            sites.append(Site('const+', node, 1, line)); sites.append(Site('const-', node, -1, line))
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'len' and len(node.args) == 1:
            sites.append(Site('len-', node, -1, line))
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ('min', 'max') and len(node.args) >= 2:
            sites.append(Site('minmax', node, 'max' if node.func.id == 'min' else 'min', line))
        elif isinstance(node, ast.If):
            sites.append(Site('if-swap', node, None, line))
    return sites

CMPFLIP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE}

def find_sites_b(tree):
    """Second mutation family, never used to guide test generation (held-out evaluation)."""
    sites = []
    for node in ast.walk(tree):
        line = getattr(node, 'lineno', 0)
        if isinstance(node, ast.Compare):
            for i, op in enumerate(node.ops):
                if type(op) in CMPFLIP: sites.append(Site('cmpflip', (node, i), CMPFLIP[type(op)], line))
        elif isinstance(node, ast.Constant) and isinstance(node.value, bool):
            sites.append(Site('boolconst', node, None, line))
        for field in ('body', 'orelse'):
            body = getattr(node, field, None)
            if isinstance(body, list) and len(body) > 1:
                for j, st in enumerate(body):
                    if isinstance(st, (ast.Assign, ast.AugAssign)) or (isinstance(st, ast.Expr) and isinstance(st.value, ast.Call)):
                        sites.append(Site('delstmt', (node, field, j), None, getattr(st, 'lineno', 0)))
    return sites

def apply_site_b(tree, idx):
    t = copy.deepcopy(tree)
    s = find_sites_b(t)[idx]
    n = s.node
    if s.kind == 'cmpflip': n[0].ops[n[1]] = s.alt()
    elif s.kind == 'boolconst': n.value = not n.value
    elif s.kind == 'delstmt': getattr(n[0], n[1])[n[2]] = ast.Pass()
    ast.fix_missing_locations(t)
    return ast.unparse(t), f'{s.kind}@L{s.line}'

def apply_site(tree, idx):
    """Returns (source of mutated copy, description) for the idx-th mutation site of tree."""
    t = copy.deepcopy(tree)
    s = find_sites(t)[idx]
    n = s.node
    if s.kind == 'cmp': n[0].ops[n[1]] = s.alt()
    elif s.kind in ('bin', 'aug'): n.op = s.alt()
    elif s.kind == 'bool': n.op = s.alt()
    elif s.kind == 'not':   # replace `not x` by `x`
        n.op = ast.UAdd(); n.operand = ast.Call(ast.Name('bool', ast.Load()), [n.operand], [])
        n.__class__ = ast.Call
        n.func, n.args, n.keywords = ast.Name('bool', ast.Load()), [n.operand.args[0]], []
        del n.op, n.operand
    elif s.kind in ('const+', 'const-'): n.value += s.alt
    elif s.kind == 'len-':
        new = ast.BinOp(copy.deepcopy(n), ast.Sub(), ast.Constant(1))
        n.__class__ = ast.BinOp; n.left, n.op, n.right = new.left, new.op, new.right; del n.func, n.args, n.keywords
    elif s.kind == 'minmax': n.func.id = s.alt
    elif s.kind == 'if-swap':
        n.test = ast.UnaryOp(ast.Not(), n.test)
    ast.fix_missing_locations(t)
    return ast.unparse(t), f'{s.kind}@L{s.line}'

def make_mutants(code, limit, seed, family='A'):
    """Deterministic sample of up to `limit` mutants of the solution source -> [(source, desc)]."""
    tree = ast.parse(code)
    finder, applier = (find_sites, apply_site) if family == 'A' else (find_sites_b, apply_site_b)
    total = len(finder(tree))
    idxs = list(range(total))
    random.Random(seed).shuffle(idxs)
    out, seen = [], set()
    base = ast.unparse(tree)
    for i in idxs:
        try: src, d = applier(tree, i)
        except Exception: continue
        if src == base or src in seen: continue
        seen.add(src); out.append((src, d))
        if len(out) >= limit: break
    return out, total
