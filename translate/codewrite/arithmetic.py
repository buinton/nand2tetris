#!/usr/bin/python3


class arithmetic:
    def __init__(self):
        self.x = 0

    def gen(self, function):
        pull = (  # Pulls 2x values from the stack First value is in @R13 second value is in d
            f'@SP\n'
            f'D=M-1\n'      # Decrement the stack pointer
            f'M=D\n'          # Set the value of the top of the stack to D
            f'A=D\n'          # Set D to the Address
            f'D=M\n'          # Set D to the top value of the stack

            f'@R13\n'
            f'M=D\n'            # Set the value of D to r13 for later use

            f'@SP\n'
            f'D=M-1\n'      # Decrement the stack pointer
            f'M=D\n'          # Set the value of the top of the stack to D
            f'A=D\n'          # Set D to the Address
            f'D=M\n'          # Set D to the top value of the stack
        )

        push = (    # Pushes the value in the D register to the stack
            f'@SP\n'
            f'A=M\n'          # Loads the top of the stack
            f'M=D\n'          # Sets the top of the stack to D
            f'@SP\n'
            f'M=M+1\n'      # Increments the stack
        )

        cond = (            # Handles boolean commands, function jumps to true with x;jmp or lets it run to use false

            f'@0\n'           # False Segment
            f'D=A\n'
            f'@PUSH{self.x}\n'
            f'0;JMP\n'        # JMP to PUSH

            f'(PASS{self.x})\n'       # True Segment
            f'D=-1\n'        # Loads all 1s (True) to D

            f'(PUSH{self.x})\n'       # Push Segment
            f'{push}'
        )

        if(function == "add"):
            out = (
                f'{pull}'        # Pulls 2x from the stack

                f'@R13\n'
                f'D=D+M\n'        # Load R13 and add it to D

                f'{push}'        # Push D to the Stack

            )
        elif(function == "sub"):
            out = (
                f'{pull}'

                f'@R13\n'
                f'D=D-M\n'        # Load R13 and sub it from D

                f'{push}'

            )

        elif(function == "eq"):
            out = (
                f'{pull}'

                f'@R13\n'
                f'D=M-D\n'        # Load R13 and sub it from D
                f'@PASS{self.x}\n'
                f'D;JEQ\n'              # Sets the address to True and if D is zero jump to it

                f'{cond}'
            )
            self.x += 1

        elif(function == "gt"):
            out = (
                f'{pull}'

                f'@R13\n'
                f'D=D-M\n'        # Load R13 and sub it from D
                f'@PASS{self.x}\n'
                f'D;JGT\n'              # Sets the address to True and if D is GT zero

                f'{cond}'
            )
            self.x += 1

        elif(function == "lt"):
            out = (
                f'{pull}'

                f'@R13\n'
                f'D=D-M\n'        # Load R13 and sub it from D
                f'@PASS{self.x}\n'
                f'D;JLT\n'              # Sets the address to True and if D is GT zero

                f'{cond}'
            )
            self.x += 1

        elif(function == "not"):
            out = (
                f'@SP\n'
                f'D=M-1\n'      # Decrement the stack pointer
                f'M=D\n'          # Set the value of the top of the stack to D
                f'A=D\n'          # Set D to the Address
                f'D=!M\n'          # Set D to the top value of the stack
                f'{push}'

            )

        elif(function == "and"):
            out = (
                f'{pull}'

                f'@R13\n'
                f'D=D&M\n'

                f'{push}'
            )

        elif(function == "or"):
            out = (
                f'{pull}'

                f'@R13\n'
                f'D=D|M\n'

                f'{push}'
            )

        elif(function == "neg"):
            out = (
                f'@SP\n'
                f'D=M-1\n'      # Decrement the stack pointer
                f'M=D\n'          # Set the value of the top of the stack to D
                f'A=D\n'          # Set D to the Address
                f'D=-M\n'          # Set D to the negative top value of the stack
                f'{push}'
            )
        return out

    def whatisx(self):
        return self.x
