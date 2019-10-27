#!/usr/bin/env python

import yaml
from glob import glob
import os
from xml.dom import minidom


allfile = set(glob('*') + glob('**/*') + glob('**/**/*')) # --b


# toc
toc = "lua-pb.toc"
f = open(toc)
needtoc = set([l.replace('\\','/') for l in f.read().splitlines() if not l.startswith('#')] + [toc])
f.close()


# xml
doc = minidom.parse('lua-pb.xml')
items = doc.getElementsByTagName('Script')
needxml = set([i.attributes['file'].value.replace('\\','/') for i in items])


ignore = list(allfile - needtoc - needxml)
ignore.sort()

#print need
f = open(".pkgmeta", 'r')
conf = yaml.load(f)
f.close()

conf['ignore'] = [t for t in (ignore) if not os.path.isdir(t)]

f = open(".pkgmeta", 'w')
yaml.dump(conf, f, default_flow_style=False)
f.close()
