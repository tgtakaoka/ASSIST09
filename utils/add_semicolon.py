#!/usr/bin/env python3

import sys

COMMENT_COLUMN: int = 23

def is_comment_line(line: str) -> bool:
    l: str = line.lstrip()
    return len(l) == 0 or l[0] == '*'

def comment_start(line: str) -> int:
    n: int = len(line)
    p: int = COMMENT_COLUMN - 1
    while p < n and line[p] != ' ':
        p += 1
    while p < n and line[p] == ' ':
        p += 1
    return p if p < n else n

def add_semicolon(line: str, p: int) -> str:
    n: int = len(line)
    if p >= n:
        return line
    comment: str = line[p:]
    line = line[:p].rstrip()
    while len(line) < COMMENT_COLUMN:
        line += ' '
    if line[-1] != ' ':
        line += ' '
    return line + '; ' + comment

while True:
    line: str = sys.stdin.readline()
    if not line:
        break
    line = line.rstrip()

    if is_comment_line(line):
        print(line)
    else:
        p: int = comment_start(line)
        print(add_semicolon(line, p))
