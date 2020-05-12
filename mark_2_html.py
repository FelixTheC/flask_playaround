#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 12.05.20
@author: eisenmenger
"""
import markdown
import pathlib


if __name__ == '__main__':
    path = pathlib.Path.cwd()
    markdown_file = path.joinpath('README.md')
    html = markdown.markdown(open(markdown_file.as_posix(), 'r').read())
    with open('markdown.html', 'w') as file:
        file.write(html)
