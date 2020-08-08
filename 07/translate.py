#!/usr/bin/python3

import codewrite
import os
import sys
import codewrite
"""
runlocation = os.path.realpath(__file__)
sys.path.append(runlocation + "/codewriter")
sys.path.append(runlocation + "/parser")
"""
print("Initalizing Output")
codewrite.new()

print("Translating Code")
codewrite.write()

print("Done")
