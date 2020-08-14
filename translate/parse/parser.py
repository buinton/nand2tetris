#!/usr/bin/python3


from . import insgen


class parse:
    # Intializes the file input and the insgen and loads the first buffer
    def __init__(self, fileclass):
        hasmorecommands = True

        self.ins = insgen.ins(fileclass.lines())

        """
        instruction = self.ins.gen()

        print(f"instruction {instruction}")
        try:
            self.c = str(instruction).split(' ')[0]
            self.a1 = str(instruction).split(' ')[1]
            self.a2 = str(instruction).split(' ')[2]
        except IndexError:
            pass
                """

    def inc(self, fileclass):  # Reloads the buffer and increments the insgen
        print("Reloading buffer and incrementing instruction")

        instruction = self.ins.gen(fileclass)
        print(f"Instruction {instruction}")
        try:
            self.c = str(instruction).split(' ')[0]
            self.a1 = str(instruction).split(' ')[1]
            self.a2 = str(instruction).split(' ')[2]
        except IndexError:
            pass
        self.ins.inc()

    # Finds the type of commands for C and returns to codewriter to all sub functions
    def cmdtypepicker(self):

        def icmdtype(argument):
            switch = {
                'add':      "C_ARITHMETIC",
                'sub':      "C_ARITHMETIC",
                'eq':       "C_ARITHMETIC",
                'lt':       "C_ARITHMETIC",
                'gt':       "C_ARITHMETIC",
                'neg':      "C_ARITHMETIC",
                'and':      "C_ARITHMETIC",
                'or':       "C_ARITHMETIC",
                'not':      "C_ARITHMETIC",
                'push':     "C_PUSH",
                'pop':      "C_POP",
                'label':    "C_LABEL",
                'goto':     "C_GOTO",
                'if-goto':  "C_IF",
                'function': "C_FUNCTION",
                'return':   "C_RETURN",
                'call':     "C_CALL"}
            return switch.get(argument)
        self.cmdtype = icmdtype(self.c)
        return self.cmdtype

    def arg1(self):  # Returns arg1 if arithmetic return just c and if not return return arg1
        if(self.cmdtype == 'C_ARITHMETIC'):
            return self.c
        elif(self.cmdtype == 'C_RETURN'):
            return
        else:
            return self.a1

    def arg2(self):  # Only return a2 if it is a function with a a2 value
        if self.cmdtype in ('C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL'):
            return self.a2
        else:
            return

    # Returns the value of has more commands to the higher function by checking if insgen has more commands
    def hasmorecommands(self):
        hmc = self.ins.hmc()
        return hmc
