#!/usr/bin/env python

import yaml
from glob import glob
import os

f = open(".pkgmeta", 'r')
conf = yaml.load(f)
f.close()

ignore = set(glob('*') + glob('**/*') + glob('**/**/*')) # --b
toc = glob('*.toc')[0]
f = open(toc)
need = set([l.replace('\\','/') for l in f.read().splitlines() if not l.startswith('#')] + [toc])
conf['ignore'] = [t for t in (ignore - need) if not os.path.isdir(t)]

f.close()

f = open(".pkgmeta", 'w')
yaml.dump(conf, f, default_flow_style=False)
f.close()
