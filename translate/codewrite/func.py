
class function:

    def __init__(self):
        self.x = 0
        pass

    def function(self, name, localvars):
        inc = (             # Intializes satck value to 0 and increments sp
            f'@0\n'
            f'D=A\n'
            f'@SP\n'
            f'A=M\n'
            f'M=D\n'
            f'@SP\n'
            f'M=M+1\n'
        )

        out = (
            f'({name})\n'         # Sets the label for call
            # Pushes localvar zeroes to the stack and increments
            f'{inc * int(localvars)}'

        )
        return out

    def call(self, funcname, argn):
        inc = (
            '@SP\n'
            'A=M\n'
            'M=D\n'
            '@SP\n'
            'M=M+1\n'
        )

        out = (
            f'@RETURN{self.x}\n'
            f'D=A\n'
            f'{inc}'

            f'@LCL\n'         # Push LCL
            f'D=M\n'
            f'{inc}'

            f'@ARG\n'         # Push ARG
            f'D=M\n'
            f'{inc}'

            f'@THIS\n'         # PUSH THIS
            f'D=M\n'
            f'{inc}'

            f'@THAT\n'         # Push THAT
            f'D=M\n'
            f'{inc}'

            f'@5\n'               # Calculate ARG by SP - 5 - argn
            f'D=A\n'
            f'@SP\n'
            f'D=M-D\n'
            f'@{argn}\n'
            f'D=D-A\n'
            f'@ARG\n'
            f'M=D\n'

            f'@SP\n'          # Sets LCL to SP
            f'D=M\n'
            f'@LCL\n'
            f'M=D\n'

            f'@{funcname}\n'  # Acutally Jumps to FUNC
            f'0;JMP\n'

            f'(RETURN{self.x})\n'


        )
        self.x += 1
        return out

    def funcreturn(self):
        out = (
            f'@LCL\n'     # Load value of local into D
            f'D=M\n'
            f'@R13\n'     # Save local to R13
            f'M=D\n'

            f'@5\n'
            f'A=D-A\n'     # Subtact 5 from local and jump to it
            f'D=M\n'       # Save the return address to D
            f'@R14\n'
            f'M=D\n'       # Save D to R14

            f'@SP\n'      # Dec SP and load value into D
            f'D=M-1\n'
            f'M=D\n'
            f'A=D\n'
            f'D=M\n'

            f'@ARG\n'     # Loads the top value of the global stack/ local stack
            f'A=M\n'      # Sets the address
            f'M=D\n'      # top of the arg to return the value produced by the function

            f'@ARG\n'       # Sets SP to ARG
            f'D=M\n'
            f'@SP\n'
            f'M=D\n'

            '@SP\n'     # Increment the stack pointer, the stack is now in a ready to use state
            'M=M+1\n'

            f'@R13\n'
            f'D=M\n'
            f'@1\n'
            f'A=D-A\n'     # Subtact 1 from local and jump to it
            f'D=M\n'       # Save the THAT to be restored to D
            f'@THAT\n'      # Restore THAT
            f'M=D\n'

            f'@R13\n'
            f'D=M\n'
            f'@2\n'
            f'A=D-A\n'     # Subtact 2 from local and jump to it
            f'D=M\n'       # Save the THIS to be restored to D
            f'@THIS\n'      # Restore THIS
            f'M=D\n'

            f'@R13\n'
            f'D=M\n'
            f'@3\n'
            f'A=D-A\n'     # Subtact 3 from local and jump to it
            f'D=M\n'       # Save the ARG to be restored to D
            f'@ARG\n'      # Restore ARG
            f'M=D\n'

            f'@R13\n'
            f'D=M\n'
            f'@4\n'
            f'A=D-A\n'     # Subtact 4 from local and jump to it
            f'D=M\n'       # Save the LCL to be restored to D
            f'@LCL\n'      # Restore LCL
            f'M=D\n'

            f'@R14\n'     # Load the return address and jump to it
            f'A=M\n'
            f'0;JMP\n'
        )

        return out
