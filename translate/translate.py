#!/usr/bin/python3

import codewrite
import os
import sys
import codewrite
import parse
"""
runlocation = os.path.realpath(__file__)
sys.path.append(runlocation + "/codewriter")
sys.path.append(runlocation + "/parser")
"""
print("Initalizing Output")
fileclass = parse.fileio()


print("Translating Code")
codewrite.write(fileclass)

print("Done")
