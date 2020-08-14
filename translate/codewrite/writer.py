#!/usr/bin/python3
'import codewrite.parse.finput as finput'
import parse
import sys


def new():
    filename = sys.argv[1]
    outfile = filename.split('.')[0] + '.asm'
    print(f"Writing to: {outfile}")
    global output
    output = open(outfile, "w")


def save(input):
    print(f"Saved: {input}")
    output.write(input)
