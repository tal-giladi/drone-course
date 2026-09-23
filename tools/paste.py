# -*- coding: utf-8 -*-
"""paste.py <lesson.md> ... : run each lesson's ## Code python block and splice the
real stdout into the ```text block that follows it."""
import io, os, re, subprocess, sys, tempfile


def do(p):
    s = io.open(p, encoding='utf-8').read()
    m0 = re.search(r'^## Code\b.*?^```python\n(.*?)^```', s, re.S | re.M)
    if not m0:
        return print('%s: no python block' % p)
    fd, tmp = tempfile.mkstemp(suffix='.py', text=True)
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(m0.group(1))
    env = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONUTF8='1')
    r = subprocess.run([sys.executable, tmp], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=env)
    os.unlink(tmp)
    if r.returncode:
        return print('%s: FAILED\n%s' % (p, r.stderr))
    real = r.stdout.rstrip('\n')
    m = re.search(r'(^Output:\n\n```text\n)(.*?)(^```)', s, re.S | re.M)
    if not m:
        return print('%s: no "Output:" text block' % p)
    s = s[:m.start(2)] + real + '\n' + s[m.start(3):]
    io.open(p, 'w', encoding='utf-8', newline='\n').write(s)
    print('%s: spliced %d lines' % (p, len(real.splitlines())))


for a in sys.argv[1:]:
    do(a)
