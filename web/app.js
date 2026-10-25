'use strict';
// C# LeetCode (offline): single-page UI. Talks to the local server's /api.

const $ = (s, el = document) => el.querySelector(s);
const view = $('#view');
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const store = {
  get(k, d) { try { const v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); } catch { return d; } },
  set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch { } },
};
async function api(path, opts) {
  const r = await fetch('/api' + path, opts);
  if (!r.ok) {
    const detail = r.status === 404 ? '' : (await r.text().catch(() => '')).slice(0, 400);
    throw new Error(r.status === 404 ? 'Not found' : 'Server error ' + r.status + (detail ? ': ' + detail : ''));
  }
  return r.status === 204 ? null : (r.headers.get('content-type') || '').includes('json') ? r.json() : r.text();
}
function toast(msg) { const t = $('#toast'); t.textContent = msg; t.classList.add('show'); clearTimeout(toast.t); toast.t = setTimeout(() => t.classList.remove('show'), 1800); }

// ---------- theme ----------
function applyTheme(t) {
  document.documentElement.dataset.theme = t;
  if (window.monaco) monaco.editor.setTheme(t === 'light' ? 'vs' : 'vs-dark');
}
let theme = store.get('theme', 'dark');
applyTheme(theme);
$('#theme').onclick = () => { theme = theme === 'dark' ? 'light' : 'dark'; store.set('theme', theme); applyTheme(theme); };

// ---------- cloud backup (git remote for userdata/, see README) ----------
let syncInfo = null;
function paintSync(i) {
  syncInfo = i;
  const b = $('#sync');
  b.className = 'icon-btn' + (i.enabled ? ' ' + (i.state === 'idle' ? 'ok' : i.state) : '');
  b.title = !i.gitAvailable ? 'Cloud backup needs git (https://git-scm.com)' : !i.enabled ? 'Cloud backup: not set up (click)'
    : `Cloud backup → ${i.remote}\n${i.message || 'ready'}${i.last ? '\nlast: ' + new Date(i.last).toLocaleString() : ''}`;
}
async function refreshSync() { try { paintSync(await api('/sync')); } catch { } }
async function watchSync() {      // after a successful submission: wait for the background backup and report
  if (!syncInfo || !syncInfo.enabled) return;
  for (let k = 0; k < 40; k++) {
    await new Promise(r => setTimeout(r, 1500));
    const i = await api('/sync').catch(() => null); if (!i) return; paintSync(i);
    if (i.state === 'ok') return toast('☁ Backed up to the cloud');
    if (i.state === 'error') return toast('☁ ' + i.message);
  }
}
$('#sync').onclick = async () => {
  const i = await api('/sync');
  if (!i.gitAvailable) return alert('Cloud backup needs git. Install it from https://git-scm.com, then restart this app.');
  if (!i.enabled) {
    const url = prompt('Back up your code and progress to a private Git repository after every solved problem.\n\n' +
      '1. Create an EMPTY PRIVATE repository (free) on GitHub / GitLab / Bitbucket.\n' +
      '2. Paste its URL here (https://github.com/you/leetcode-backup.git).\n\n' +
      'It uses the git login already on this computer. See README for details.');
    if (!url) return;
    toast('Connecting…');
    const r = await api('/sync/setup', jsonBody({ remote: url }));
    if (!r.ok) return alert(r.error);
    toast('☁ Cloud backup is on'); watchSync(); return refreshSync();
  }
  const a = prompt(`Cloud backup is on (${i.remote}).\n${i.message || ''}\n\nType  now  to back up right now, or  off  to disconnect. Leave empty to cancel.`, 'now');
  if (a === 'now') { await api('/sync/now', { method: 'POST' }); toast('Backing up…'); paintSync({ ...i, state: 'running', message: 'Backing up...' }); watchSync(); }
  else if (a === 'off') { await api('/sync', { method: 'DELETE' }); toast('Cloud backup disconnected (your data stays on this computer and in the repo)'); refreshSync(); }
};
refreshSync();

// ---------- state ----------
let problems = [];
async function loadProblems() {
  problems = await api('/problems');
  const solved = problems.filter(p => p.status === 'solved').length;
  $('#stats').textContent = `${solved} / ${problems.length} solved`;
}

// ---------- router ----------
let cleanup = null;
async function route() {
  if (cleanup) { try { await cleanup(); } catch { } cleanup = null; }
  $('#nav-center').innerHTML = '';
  const m = location.hash.match(/^#\/problem\/(.+)$/);
  try {
    await loadProblems();
    if (m) await problemPage(decodeURIComponent(m[1])); else listPage();
  } catch (e) {
    view.innerHTML = `<div class="fatal"><h2>Can't reach the local server</h2><p>${esc(e.message)}</p><p>If you closed the black launcher window, double-click the launcher again.</p></div>`;
  }
}
window.addEventListener('hashchange', route);
route();

// ---------- problem list ----------
function listPage() {
  const topics = [...new Set(problems.flatMap(p => p.topics))].sort();
  const f = store.get('filters', { q: '', topic: '', status: '', tests: '' });
  view.innerHTML = `<div class="list-page"><div class="list-wrap">
    <div class="toolbar">
      <input id="q" placeholder="Search by title or number…" value="${esc(f.q)}" autofocus>
      <select id="topic"><option value="">All topics</option>${topics.map(t => `<option ${t === f.topic ? 'selected' : ''}>${esc(t)}</option>`).join('')}</select>
      <select id="status"><option value="">All status</option><option value="todo">Todo</option><option value="attempted">Attempted</option><option value="solved">Solved</option></select>
      <select id="tests"><option value="">Any tests</option><option value="yes">Has test suite</option><option value="no">No test suite</option></select>
      <button class="btn" id="rand">Pick random</button>
    </div>
    <div class="progress-bar"><div id="pb"></div></div>
    <div class="count" id="count"></div>
    <table class="problems"><tbody id="rows"></tbody></table>
  </div></div>`;
  $('#status').value = f.status; $('#tests').value = f.tests;
  let shown = [];
  const render = () => {
    const q = $('#q').value.trim().toLowerCase(), topic = $('#topic').value, st = $('#status').value, ts = $('#tests').value;
    store.set('filters', { q: $('#q').value, topic, status: st, tests: ts });
    shown = problems.filter(p =>
      (!q || p.title.toLowerCase().includes(q) || String(p.id) === q || String(p.id).startsWith(q)) &&
      (!topic || p.topics.includes(topic)) &&
      (!st || (st === 'todo' ? !p.status : p.status === st)) &&
      (!ts || (ts === 'yes' ? p.tests > 0 : p.tests === 0)));
    $('#rows').innerHTML = shown.map(p => `<tr>
      <td class="st">${p.status === 'solved' ? '<span class="solved" title="Solved">✔</span>' : p.status === 'attempted' ? '<span class="attempted" title="Attempted">◔</span>' : ''}</td>
      <td class="title"><a href="#/problem/${encodeURIComponent(p.folder)}">${p.id}. ${esc(p.title)}</a></td>
      <td class="topics">${esc(p.topics.join(', '))}</td>
      <td class="tests">${p.tests ? p.tests + ' tests' : 'no tests'}</td>
      <td class="diff medium">Medium</td></tr>`).join('') || '<tr><td class="empty">No problems match.</td></tr>';
    const solved = problems.filter(p => p.status === 'solved').length;
    $('#count').textContent = `${shown.length} problems shown · ${solved} of ${problems.length} solved`;
    $('#pb').style.width = (100 * solved / problems.length) + '%';
  };
  for (const id of ['q', 'topic', 'status', 'tests']) $('#' + id).addEventListener('input', render);
  $('#rand').onclick = () => { const pool = shown.length ? shown : problems; const p = pool[Math.floor(Math.random() * pool.length)]; location.hash = '#/problem/' + encodeURIComponent(p.folder); };
  render();
}

// ---------- Monaco ----------
let monacoReady = null;
function loadMonaco() {
  if (monacoReady) return monacoReady;
  monacoReady = new Promise((resolve, reject) => {
    const base = new URL('vendor/monaco/vs', location.href).href;
    window.MonacoEnvironment = {
      getWorkerUrl: () => 'data:text/javascript;charset=utf-8,' + encodeURIComponent(
        `self.MonacoEnvironment={baseUrl:'${new URL('vendor/monaco/', location.href).href}'};importScripts('${base}/base/worker/workerMain.js');`),
    };
    require.config({ paths: { vs: base } });
    require(['vs/editor/editor.main'], () => resolve(window.monaco), reject);
  });
  return monacoReady;
}
const cssLink = document.createElement('link');
cssLink.rel = 'stylesheet'; cssLink.href = 'vendor/monaco/vs/editor/editor.main.css'; document.head.appendChild(cssLink);

// ---------- problem page ----------
function makeSplit(gutter, a, b, dir, minA, minB) {
  gutter.addEventListener('pointerdown', e => {
    e.preventDefault(); gutter.setPointerCapture(e.pointerId); gutter.classList.add('drag');
    const parent = gutter.parentElement.getBoundingClientRect();
    const mv = ev => {
      const total = dir === 'v' ? parent.width : parent.height;
      let pos = dir === 'v' ? ev.clientX - parent.left : ev.clientY - parent.top;
      pos = Math.max(minA, Math.min(total - minB - 8, pos));
      if (dir === 'v') a.style.flex = `0 0 ${pos}px`; else b.style.flex = `0 0 ${total - pos - 8}px`;
      window.dispatchEvent(new Event('resize'));
    };
    const up = () => { gutter.classList.remove('drag'); gutter.removeEventListener('pointermove', mv); gutter.removeEventListener('pointerup', up); };
    gutter.addEventListener('pointermove', mv); gutter.addEventListener('pointerup', up);
  });
}

async function problemPage(folder) {
  const [p, mon] = await Promise.all([api('/problems/' + encodeURIComponent(folder)), loadMonaco()]);
  const idx = problems.findIndex(x => x.folder === folder);
  const prev = problems[idx - 1], next = problems[idx + 1];
  document.title = `${p.id}. ${p.title} · C# LeetCode`;

  $('#nav-center').innerHTML = `
    ${prev ? `<a class="icon-btn" href="#/problem/${encodeURIComponent(prev.folder)}" title="Previous: ${esc(prev.title)}">◀</a>` : ''}
    <button class="btn run" id="run" title="Run the first 10 test cases">▶ Run<kbd>Ctrl+'</kbd></button>
    <button class="btn submit" id="submit" title="Run all test cases">Submit<kbd>Ctrl+↵</kbd></button>
    ${next ? `<a class="icon-btn" href="#/problem/${encodeURIComponent(next.folder)}" title="Next: ${esc(next.title)}">▶</a>` : ''}`;

  view.innerHTML = `<div class="split">
    <section class="pane" id="left">
      <div class="tabs">
        <button class="tab active" data-tab="desc">Description</button>
        <button class="tab" data-tab="edit">Editorial</button>
        <button class="tab" data-tab="subs">Submissions</button>
      </div>
      <div class="tabbody" id="tabbody"></div>
    </section>
    <div class="gutter v" id="g1"></div>
    <div id="right" style="display:flex;flex-direction:column;min-width:0;min-height:0;flex:1">
      <section class="pane" id="editor-pane" style="flex:1">
        <div class="tabs"><span style="color:var(--text-strong);padding:0 8px">&lt;/&gt; Code · C#</span><span class="spacer"></span>
          <label><input type="checkbox" id="unordered"> ignore result order</label>
          <select id="fontsize">${[12, 13, 14, 16, 18, 20].map(n => `<option ${n === store.get('fontSize', 14) ? 'selected' : ''}>${n}</option>`).join('')}</select>
          <button class="btn small ghost" id="reset">Reset</button>
        </div>
        <div id="editor-wrap"><div id="editor"></div></div>
      </section>
      <div class="gutter h" id="g2"></div>
      <section class="pane" id="console">
        <div class="tabs"><span style="color:var(--text-strong);padding:0 8px">Console</span></div>
        <div class="console-body" id="out"><span class="hint">Run your code to see results here. <b>Run</b> checks the first 10 test cases, <b>Submit</b> checks all ${p.tests || 0}.</span></div>
      </section>
    </div></div>`;

  // --- left tabs ---
  const body = $('#tabbody');
  const bodyMd = md => {
    const stripped = md.replace(/^# .*\n/, '').replace(/^\*\*Difficulty:\*\*.*\n/m, '').replace(/^\*\*Topics:\*\*.*\n/m, '').replace(/^\*\*Link \(online only\):\*\*.*\n/m, '');
    // The pack's statements lost their superscripts ("10^4" reads "104", "2^31 - 1" reads "231 - 1"). Restore the
    // unambiguous forms in the Constraints list: 10^3..10^18 and 2^15/16/31/32/63.
    const i = stripped.indexOf('**Constraints:**');
    const fixed = i < 0 ? stripped : stripped.slice(0, i) + stripped.slice(i).split('\n').map(l => !/^\s*[-*]\s/.test(l) ? l :
      l.replace(/(?<![\w.^])10(3|4|5|6|7|8|9|1[0-8])(?![\w.])/g, '10<sup>$1</sup>').replace(/(?<![\w.^])2(15|16|31|32|63)(?![\w.])/g, '2<sup>$1</sup>')).join('\n');
    return marked.parse(fixed);
  };
  const statusChip = () => p.status === 'solved' ? '<span class="chip st-solved">✔ Solved</span>' : p.status === 'attempted' ? '<span class="chip">Attempted</span>' : '';
  const showDesc = () => {
    body.innerHTML = `<h1>${p.id}. ${esc(p.title)}</h1>
      <div class="meta"><span class="chip diff">Medium</span>${statusChip()}${p.topics.map(t => `<span class="chip">${esc(t)}</span>`).join('')}
      ${p.tests ? '' : '<span class="chip">no test suite — check the examples by hand</span>'}
      ${p.examplesOnly ? '<span class="chip" title="The dataset has no tests for this problem, so the tests are the examples from the statement. Passing them is a smoke test, not proof of correctness.">examples only</span>' : ''}</div>
      <div class="md">${bodyMd(p.readme)}</div>
      <p class="hint" style="margin-top:24px">${p.tests ? `${p.tests} automated test cases · ` : ''}<a href="${esc(p.link)}" target="_blank" rel="noopener">Open on leetcode.com ↗</a>
      ${p.tests ? '' : ` · <a href="#" id="mark">${p.status === 'solved' ? 'Mark as unsolved' : 'Mark as solved'}</a>`}</p>`;
    const mk = $('#mark');
    if (mk) mk.onclick = async e => { e.preventDefault(); await api(`/problems/${encodeURIComponent(folder)}/mark`, jsonBody({ solved: p.status !== 'solved' })); p.status = p.status === 'solved' ? null : 'solved'; await loadProblems(); showDesc(); };
  };
  const showEditorial = async (confirmed) => {
    if (!p.hasEditorial) { body.innerHTML = '<div class="empty">No editorial available for this problem.</div>'; return; }
    if (!confirmed) {
      body.innerHTML = '<div class="spoiler"><h2>Editorial</h2><p>Contains spoilers: approaches and full solutions.<br>Give it your best shot first.</p><button class="btn" id="reveal">Show editorial</button></div>';
      $('#reveal').onclick = () => showEditorial(true); return;
    }
    body.innerHTML = '<span class="spin"></span>Loading…';
    body.innerHTML = '<div class="md">' + marked.parse(await api(`/problems/${encodeURIComponent(folder)}/editorial`)) + '</div>';
  };
  const showSubs = () => {
    if (!p.submissions.length) { body.innerHTML = '<div class="empty">No submissions yet. Press Submit to run every test case.</div>'; return; }
    body.innerHTML = `<table class="sublist"><tr><th>Time</th><th>Result</th><th>Passed</th><th>Runtime</th></tr>${p.submissions.map((s, i) => `
      <tr class="click" data-i="${i}"><td>${esc(new Date(s.time).toLocaleString())}</td>
      <td class="${s.status === 'accepted' ? 'accepted' : 'bad'}">${esc(label(s.status))}</td><td>${s.passed}/${s.total}</td><td>${s.ms} ms</td></tr>`).join('')}</table>
      <p class="hint">Click a submission to load its code into the editor.</p>`;
    body.querySelectorAll('tr.click').forEach(tr => tr.onclick = () => { editor.setValue(p.submissions[tr.dataset.i].code); toast('Loaded submission into editor'); });
  };
  const tabs = { desc: showDesc, edit: () => showEditorial(false), subs: showSubs };
  document.querySelectorAll('#left .tab').forEach(b => b.onclick = () => {
    document.querySelectorAll('#left .tab').forEach(x => x.classList.toggle('active', x === b)); tabs[b.dataset.tab]();
  });
  showDesc();

  // --- editor ---
  const fontSize = store.get('fontSize', 14);
  const editor = mon.editor.create($('#editor'), {
    value: p.code ?? p.starter, language: 'csharp', theme: theme === 'light' ? 'vs' : 'vs-dark',
    automaticLayout: true, fontSize, minimap: { enabled: false }, scrollBeyondLastLine: false,
    tabSize: 4, insertSpaces: true, renderWhitespace: 'none', padding: { top: 10 },
  });
  const model = editor.getModel();
  $('#fontsize').onchange = e => { const n = +e.target.value; store.set('fontSize', n); editor.updateOptions({ fontSize: n }); };
  $('#unordered').checked = store.get('unordered:' + folder, !!p.unordered);   // statements that accept any order default to on
  $('#unordered').onchange = e => store.set('unordered:' + folder, e.target.checked);
  $('#reset').onclick = async () => {
    if (!confirm('Reset to the starter code? Your current code will be discarded.')) return;
    await api(`/problems/${encodeURIComponent(folder)}/code`, { method: 'DELETE' });
    p.code = null; editor.setValue(p.starter); mon.editor.setModelMarkers(model, 'csc', []);
  };
  let saveT;
  const save = () => api(`/problems/${encodeURIComponent(folder)}/code`, { method: 'PUT', body: editor.getValue() }).catch(() => { });
  editor.onDidChangeModelContent(() => { clearTimeout(saveT); saveT = setTimeout(save, 700); });
  mon.editor.setTheme(theme === 'light' ? 'vs' : 'vs-dark');

  // --- run / submit ---
  const out = $('#out');
  let busy = false;
  const label = s => ({ accepted: 'Accepted', wrong_answer: 'Wrong Answer', compile_error: 'Compile Error', runtime_error: 'Runtime Error', timeout: 'Time Limit Exceeded', no_tests: 'No test suite' }[s] || s);
  async function exec(submit) {
    if (busy) return; busy = true;
    $('#run').disabled = $('#submit').disabled = true;
    out.innerHTML = `<span class="spin"></span>${submit ? 'Judging all test cases' : 'Running'}… <span class="hint">(compiling takes a few seconds)</span>`;
    mon.editor.setModelMarkers(model, 'csc', []);
    clearTimeout(saveT);
    try {
      const r = await api(`/problems/${encodeURIComponent(folder)}/run`, jsonBody({ code: editor.getValue(), submit, unordered: $('#unordered').checked }));
      showResult(r, submit);
      if (r.status === 'accepted' && submit) watchSync();
      if (submit) { const fresh = await api('/problems/' + encodeURIComponent(folder)); p.status = fresh.status; p.submissions = fresh.submissions; await loadProblems(); if (document.querySelector('#left .tab.active').dataset.tab === 'subs') showSubs(); }
    } catch (e) { out.innerHTML = `<div class="box err">${esc(e.message)}</div>`; }
    busy = false; $('#run').disabled = $('#submit').disabled = false;
  }
  function stdoutBlock(r) {
    return r.stdout ? `<div class="lbl">Stdout</div><div class="box">${esc(r.stdout)}</div>` : '';
  }
  function showResult(r, submit) {
    const kind = submit ? 'Submission' : 'Run';
    if (r.status === 'compile_error') {
      mon.editor.setModelMarkers(model, 'csc', (r.errors || []).map(e => ({
        severity: mon.MarkerSeverity.Error, message: `${e.code}: ${e.message}`,
        startLineNumber: e.line, startColumn: e.col, endLineNumber: e.line, endColumn: Math.max(e.col + 1, model.getLineMaxColumn(e.line)),
      })));
      out.innerHTML = `<div class="result-title bad">Compile Error</div><div class="result-sub">${(r.errors || []).length} error(s)</div>` +
        ((r.errors || []).map(e => `<div class="box err" style="margin-bottom:6px;cursor:pointer" data-l="${e.line}" data-c="${e.col}">Line ${e.line}, col ${e.col}: ${esc(e.code)} ${esc(e.message)}</div>`).join('') ||
          `<div class="box err">${esc(r.raw)}</div>`);
      out.querySelectorAll('[data-l]').forEach(d => d.onclick = () => { editor.revealLineInCenter(+d.dataset.l); editor.setPosition({ lineNumber: +d.dataset.l, column: +d.dataset.c }); editor.focus(); });
      return;
    }
    if (r.status === 'no_tests') {
      out.innerHTML = `<div class="result-title">No test suite</div><div class="result-sub">${esc(r.message)}</div><p>Check your code against the examples in the description, then mark it solved from the Description tab.</p>`;
      return;
    }
    if (r.status === 'runtime_error' && !r.failures) {
      out.innerHTML = `<div class="result-title bad">Runtime Error</div><div class="box err">${esc(r.raw)}</div>`; return;
    }
    if (r.status === 'timeout') {
      out.innerHTML = `<div class="result-title bad">Time Limit Exceeded</div><div class="result-sub">${r.passed} test(s) passed before test #${r.timeout.i} took over ${r.timeout.limit || 10} s.</div>
        <div class="lbl">Last input</div><div class="box">${esc(r.timeout.input)}</div>${stdoutBlock(r)}`; return;
    }
    const total = r.total, ok = r.status === 'accepted';
    let h = `<div class="result-title ${ok ? 'accepted' : 'bad'}">${esc(label(r.status))}</div>
      <div class="result-sub">${r.passed} / ${total} testcases passed · ${r.ms} ms${submit ? '' : ' (Run: first ' + total + ' cases)'}</div>`;
    if (!ok) {
      h += `<div class="case-tabs">${r.failures.map((f, i) => `<button class="case-tab ${i ? '' : 'active'}" data-i="${i}"><span class="dot"></span>Case ${f.i}</button>`).join('')}</div><div id="case"></div>`;
    }
    if (r.skipped) h += `<p class="hint">${r.skipped} generated test(s) skipped (invalid input for LeetCode types).</p>`;
    if (r.inplace) h += `<p class="hint">In-place problem: the dataset only checks that your code runs without throwing; verify the result against the README examples.</p>`;
    if (r.orderOnly && !$('#unordered').checked) h += `<p class="hint">${r.orderOnly} failure(s) have the right elements in a different order. If this problem accepts any order, tick “ignore result order”.</p>`;
    if (r.failCount > r.failures.length) h += `<p class="hint">Showing the first ${r.failures.length} of ${r.failCount} failures.</p>`;
    h += stdoutBlock(r);
    out.innerHTML = h;
    if (!ok) {
      const cases = out.querySelectorAll('.case-tab');
      const showCase = i => {
        cases.forEach(c => c.classList.toggle('active', +c.dataset.i === i));
        const f = r.failures[i];
        $('#case').innerHTML = `<div class="lbl">Input</div><div class="box">${esc(f.input)}</div>${f.step ? `<div class="lbl">Failed at</div><div class="box">${esc(f.step)}</div>` : ''}` + (f.error
          ? `<div class="lbl">Error</div><div class="box err">${esc(f.error)}</div>`
          : `<div class="lbl">Output</div><div class="box err">${esc(f.got)}</div><div class="lbl">Expected</div><div class="box">${esc(f.expected)}</div>${f.orderOnly ? '<div class="hint">Same elements, different order.</div>' : ''}`);
      };
      cases.forEach(c => c.onclick = () => showCase(+c.dataset.i)); showCase(0);
    }
  }
  $('#run').onclick = () => exec(false);
  $('#submit').onclick = () => exec(true);
  editor.addCommand(mon.KeyMod.CtrlCmd | mon.KeyCode.Quote, () => exec(false));
  editor.addCommand(mon.KeyMod.CtrlCmd | mon.KeyCode.Enter, () => exec(true));

  // --- splitters ---
  makeSplit($('#g1'), $('#left'), $('#right'), 'v', 280, 360);
  makeSplit($('#g2'), $('#editor-pane'), $('#console'), 'h', 120, 80);

  cleanup = async () => { clearTimeout(saveT); if (editor.getValue() !== (p.code ?? p.starter)) await save(); editor.dispose(); document.title = 'C# LeetCode (offline)'; };
}

function jsonBody(o) { return { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(o) }; }
