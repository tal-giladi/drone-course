"""Extract the ```python block under '## Code' in a lesson and run it.

Usage: py runcode.py <lesson.md>
Prints the real stdout so it can be pasted into the Expected-result block.
"""
import re, subprocess, sys, os, tempfile

path = sys.argv[1]
src = open(path, encoding='utf-8').read()
m = re.search(r'^## Code\b.*?^```python\n(.*?)^```', src, re.S | re.M)
if not m:
    sys.exit('no python block under ## Code in ' + path)
code = m.group(1)
fd, tmp = tempfile.mkstemp(suffix='.py', text=True)
with os.fdopen(fd, 'w', encoding='utf-8') as f:
    f.write(code)
env = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONUTF8='1')
r = subprocess.run([sys.executable, tmp], capture_output=True, text=True,
                   encoding='utf-8', errors='replace', env=env)
os.unlink(tmp)
if r.returncode:
    print('--- STDERR ---')
    print(r.stderr)
    sys.exit(1)
print(r.stdout, end='')
