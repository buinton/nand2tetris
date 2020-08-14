#!/usr/bin/python3


import sys
from os import walk

#!/usr/bin/python3

import os
import sys


class fileio:

    def __init__(self):
        self.path = sys.argv[1]         # Grabs the path from stdin

        f = []
        isdir = False
        if(os.path.isdir(self.path)):   # Checks if its a directory
            # Makes sure that the directory has a slash at the end
            if self.path.endswith('/'):
                pass
            else:
                self.path += '/'
            isdir = True
            for (dirpath, dirnames, filenames) in os.walk(self.path):
                # If its a dir then walk through all files and write them to a list
                f.extend(filenames)
                break
        else:
            # Else just write the path
            print("Not dir")
            f.append(self.path.split('/')[-1])

        print(f'All files in the folder: \n{f}')

        files = []
        for i in f:
            # Iterate through the list of files and sees which ones end with vm and writes them to files
            if i.endswith('.vm'):
                files.append(i)
                continue

        print(f'All VM files in the folder: \n{files}')

        bootstrap = True
        if bootstrap is True:
            self.out = ['call Sys.init 0']
        else:
            self.out = []
        print(f"Writing Bootstrap Code:\n{self.out}")

        if isdir is True:
            # If multiple files open all and write them to the list
            for i in files:
                file = open(self.path + i, 'r')
                self.out.extend(file.readlines())
        else:
            # If one file open it and write to the list
            file = open(self.path, 'r')
            self.out = file.readlines()

        # Generates the outfile
        outfilename = self.path.split('/')[-2]
        if isdir is True:
            outfile = self.path + outfilename + '.asm'
        else:
            outfile = outfilename.split('.')[1] + '.asm'
        print(f"Outfile: {outfile}")
        self.outfile = open(outfile, 'w')

    def lines(self):    # Returns the lines generated during init
        return self.out

    def save(self, data):
        self.outfile.write(str(data))
        print(f"Saved:\n{data}")
