#!/usr/bin/env python3
from os.path import join, dirname
import markdown

template = join(dirname(__file__), "index.template.html")
dest = join(dirname(__file__), "index.html")
src = join(dirname(__file__), "index.md")

def line_process(text):
    v = text.split('\n')
    new = list()
    in_list = False
    for line in v:
        if line.startswith('- '):
            if not in_list:
                in_list = True
                new.append('<ul>')
            line = f'<li>{line[2:]}</li>'
        elif in_list:
            new.append('</ul>')
            in_list = False

        new.append(line)

    return '\n'.join(new)

res = markdown.markdown(line_process(open(src).read()))
            

template = open(template, 'r').read()
open(dest, 'w').write(template.replace("##BODY", res))
