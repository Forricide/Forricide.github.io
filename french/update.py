#!/usr/bin/env python3
from os.path import join, dirname
import markdown

template = join(dirname(__file__), "index.template")
dest = join(dirname(__file__), "index.html")
src = join(dirname(__file__), "index.md")
res = markdown.markdown(open(src).read())

template = open(template, 'r').read()
open(dest, 'w').write(template.replace("##BODY", res))
