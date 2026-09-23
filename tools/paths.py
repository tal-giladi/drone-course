# -*- coding: utf-8 -*-
"""paths.py [prefix ...] : print every lesson id and its file path, so a lesson
being written can link to lessons that do not exist yet without guessing slugs.

    py tools/paths.py          # everything
    py tools/paths.py 04 17    # just those modules
"""
import json, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
g = json.load(open(os.path.join(root, 'curriculum', 'graph.json'), encoding='utf-8'))
pre = tuple(sys.argv[1:])
for k, n in g['nodes'].items():
    if not pre or k.startswith(pre):
        print('%-7s %s' % (k, n.get('path')))
