#!/usr/bin/python3


"""import codewrite.stack as stack
import codewrite.parse.parser as parser
import codewrite.write as writer
import codewrite.arithmetic as arithmetic"""
import time
from codewrite import writer, arithmetic, stack, flow, func
from parse import parser


def write(fileclass):

    print("Initalizing Parser")
    code = parser.parse(fileclass)  # Call the parser
    arith = arithmetic()   # Initalize the arithmetic class
    zflow = flow.pflow()
    zfunc = func.function()
    x = True
    while(x == True):      # Checks the parsers has more commands variable

        print("Incrementing code")
        code.inc(fileclass)

        if (code.hasmorecommands() == True):
            print(f"arith x is {arith.whatisx()}")
            # Load the command type and *args to local buffer
            cmdtype = code.cmdtypepicker()
            a1 = code.arg1()
            a2 = code.arg2()

            print(f"cmdtype {cmdtype}")
            print(f"a1 {a1}")
            print(f"a2 {a2}")
            if(cmdtype == "C_PUSH"):                # If it is a instruction call apprioate module
                out = stack.push(a1, a2)
            elif(cmdtype == "C_POP"):
                out = stack.pop(a1, a2)
            elif(cmdtype == "C_ARITHMETIC"):
                out = arith.gen(a1)
            elif(cmdtype == "C_LABEL"):
                out = zflow.label(a1)
            elif(cmdtype == "C_GOTO"):
                out = zflow.goto(a1)
            elif(cmdtype == "C_IF"):
                out = zflow.ifgoto(a1)
            elif(cmdtype == "C_FUNCTION"):
                out = zfunc.function(a1, a2)
            elif(cmdtype == "C_RETURN"):
                out = zfunc.funcreturn()
            elif(cmdtype == "C_CALL"):
                out = zfunc.call(a1, a2)

                # Saves the out buffer
            fileclass.save(str(out))
            # Increments the instruction
            continue
        else:
            x = False
