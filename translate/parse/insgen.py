#!/usr/bin/python3
'import codewrite.write as writer'
from codewrite import writer


class ins:
    def __init__(self, lines):  # Lines is the .readlines() of the input stream
        print("Initalizing ins")
        self.x = 0
        self.lines = lines
        self.hasmorecommands = True
        self.exit = False

    def inc(self):  # Increments the currently acitve line
        self.x += 1

    def gen(self, fileclass):  # Generates the instruction by first striping commented lines and then checking if it should increment

        self.hasmorecommands = True
        self.exit = False
        ins = ''

        while(self.exit == False):
            try:
                ins = str(self.lines[self.x].split('//')[0]).strip()
            except IndexError:   # Checks if we have reached the end of the file
                print(f"{self.x}    No More Commands")
                self.hasmorecommands = False
                self.exit = True

            if(not ins):  # Checks that there is anything in the instruction
                print(f"{self.x}    No instruction")
                self.x += 1
            # If all checks then return the instruction and inc x and set all apprioate variables
            else:

                self.hasmorecommands = True
                self.exit = True
                print(f"{self.x}    //{ins}")
                fileclass.save(f"//{ins}\n")
                return ins

    def hmc(self):  # Returns the has more varibles bool
        pass
        return self.hasmorecommands
