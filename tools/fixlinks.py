"""Rewrite every lesson-file link in the course to the id's current path.

Usage:  py fixlinks.py            report only
        py fixlinks.py --write    apply
"""
import json, os, re, sys, posixpath

os.chdir(r'C:\Users\TalGiladi\OneDrive\repos\course-creator\drone-course')
g = json.load(open('curriculum/graph.json', encoding='utf-8'))
_nodes = g['nodes'].values() if isinstance(g['nodes'], dict) else g['nodes']
PATH = {n['id']: n['path'] for n in _nodes}

# lessons removed by the 2026-09-22 trim -> the lesson that absorbed them
ABSORBED = {
    '04.07': '04.06', '04.08': '04.06', '04.09': '04.06', '04.10': '04.05',
    '05.07': '05.05', '05.08': '05.05', '05.09': '05.06', '05.10': '05.06', '05.11': '05.06',
    '06.07': '06.05', '06.08': '06.05', '06.09': '06.05', '06.10': '06.06',
    '06.11': '06.06', '06.12': '06.06',
    '07.08': '07.07', '07.09': '07.07', '07.10': '07.07', '07.11': '07.07', '07.12': '07.05',
    '08.08': '08.07', '08.09': '08.07', '08.10': '08.04', '08.11': '08.04', '08.12': '08.07',
    '09.06': '09.04', '09.07': '09.05', '09.08': '09.01', '09.09': '09.04', '09.10': '09.05',
    '10.06': '10.04', '10.07': '10.05', '10.08': '10.05', '10.09': '10.05', '10.10': '10.05',
    '11.07': '11.06', '11.08': '11.02', '11.09': '11.06', '11.10': '11.06',
    '12.07': '12.05', '12.08': '12.02', '12.09': '12.06', '12.10': '12.06', '12.11': '12.06',
    '13.06': '13.04', '13.07': '13.04', '13.08': '13.05', '13.09': '13.05', '13.10': '13.05',
    '14.07': '14.06', '14.08': '14.06', '14.09': '14.06', '14.10': '14.06', '14.11': '14.05',
    '15.07': '15.05', '15.08': '15.05', '15.09': '15.06', '15.10': '15.06',
    '16.06': '16.04', '16.07': '16.04', '16.08': '16.05', '16.09': '16.03', '16.10': '16.05',
    '17.07': '17.05', '17.08': '17.05', '17.09': '17.05', '17.10': '17.04', '17.11': '17.06',
    '18.07': '18.03', '18.08': '18.03', '18.09': '18.06', '18.10': '18.06',
    '19.06': '19.05', '19.07': '19.05', '19.08': '19.05',
    'FA.05': 'FA.04', 'FA.06': 'FA.04', 'FA.07': 'FA.04', 'FA.08': 'FA.04',
    'FEL.05': 'FEL.04', 'FEL.06': 'FEL.05', 'FEL.07': 'FEL.05',
    'FEL.08': 'FEL.05', 'FEL.09': 'FEL.03',
    'FGL.02': 'FGL.01', 'FGL.04': 'FGL.02', 'FGL.05': 'FGL.03',
    'FGL.06': 'FGL.04', 'FGL.07': 'FGL.04', 'FGL.08': 'FGL.04',
    'FRA.05': 'FRA.04', 'FRA.06': 'FRA.04', 'FRA.07': 'FRA.04', 'FRA.08': 'FRA.04',
    'FOP.02': 'FOP.01', 'FOP.03': 'FOP.01', 'FOP.04': 'FOP.01',
    'FOP.05': 'FOP.01', 'FOP.06': 'FOP.02', 'FOP.07': 'FOP.03',
    'P09': 'P08', 'P10': 'P08', 'P11': 'P08', 'P12': 'P08',
}

ID_RE = re.compile(r'^((?:\d\d\.\d\d)|(?:F[A-Z]{1,3}\.\d\d)|(?:P\d\d))-')
LINK_RE = re.compile(r'(?<!!)(\[[^\]]*\])\(([^)\s]+\.md)((?:\s+"[^"]*")?)\)')

WRITE = '--write' in sys.argv
changed = total = 0

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ('.tools', 'node_modules', '.git', '.pytest_cache')]
    for fn in files:
        if not fn.endswith('.md'):
            continue
        p = os.path.join(root, fn).replace('\\', '/').lstrip('./')
        src = open(p, encoding='utf-8').read()

        def repl(m):
            global total
            text, target, title = m.groups()
            if target.startswith(('http', '#')):
                return m.group(0)
            base = posixpath.basename(target)
            hit = ID_RE.match(base)
            if not hit:
                return m.group(0)
            lid = hit.group(1)
            lid = ABSORBED.get(lid, lid)
            if lid not in PATH:
                return m.group(0)
            new = posixpath.relpath(PATH[lid], posixpath.dirname(p)) or PATH[lid]
            if new == target:
                return m.group(0)
            total += 1
            return '%s(%s%s)' % (text, new, title)

        out = LINK_RE.sub(repl, src)
        if out != src:
            changed += 1
            if WRITE:
                open(p, 'w', encoding='utf-8', newline='\n').write(out)
            else:
                print('would fix', p)

print('%d links in %d files%s' % (total, changed, '' if WRITE else ' (dry run)'))
