#!/usr/bin/env python3

import sys
import os
from random import choice

def link(url: str, text: str) -> str:
    return '\033]8;;{url}\033\\{text}\033]8;;\033\\'.format(url=url, text=text)

if len(sys.argv) != 2:
    print('give me a filename')
    sys.exit(1)

fname = sys.argv[1]
if not os.path.exists(fname):
    print('file not found')
    sys.exit(1)

with open(fname, 'r') as fh:
    content = fh.read()

line = choice((content.split(os.linesep)))
quote, author = [t.strip() for t in line.split('--')]

print(
    link('https://www.deepl.com/translator#en/de/{quote}'.format(quote=quote), quote),
    '--',
    link('https://duckduckgo.com/?q={author}'.format(author=author), author)
)
