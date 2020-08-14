
class pflow:

    def __init__(self):
        pass

    def label(self, l):
        out = (
            f"({l})\n"      # Sets a variable for the assembler
        )
        return out

    def goto(self, l):
        out = (
            f"@{l}\n"       # Loads the jump point
            f"0;JMP\n"      # Jumps to the loaded address
        )
        return out

    def ifgoto(self, l):
        out = (
            f'@SP\n'            # Dec SP and load value into D
            f'D=M-1\n'
            f'M=D\n'
            f'A=D\n'
            f'D=M\n'            # Should get the value of the top value of the stack being the output of the math function from before

            f'@R13\n'
            f'M=D\n'            # Store the data in R13 for later

            # Sets the D register to -1 for comparison with the output of the logic function
            f'D = -1\n'

            f'@R13\n'
            f'D=M&D\n'        # -1 - -1 = 0 if true
            f'@{l}\n'
            f'D;JNE\n'            # Jump to l if D is equal to zero
        )
        return out
