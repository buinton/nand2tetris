#!/usr/bin/python3

'import codewrite.pointerhandler as pointerhandler'
from codewrite import pointerhandler


def push(pointer, index=0):
    ps = pointerhandler.pointer(pointer)

    inc = (
        '@SP\n'
        'A=M\n'
        'M=D\n'
        '@SP\n'
        'M=M+1\n'
    )

    if (pointer == "constant"):
        set = (
            f"@{index}\n"
            f"D=A\n"
        )
    elif (pointer == "temp"):
        # Constant plus 5 are the temp register, vunerable af but who cares
        tempoffset = int(index) + 5
        set = (
            f"@{str(tempoffset)}\n"
            f"D=M\n"
        )
    elif (pointer == "temp"):
        # Constant plus 5 are the temp register, vunerable af but who cares
        tempoffset = int(index) + 5
        set = (
            f"@{str(tempoffset)}\n"
            f"D=M\n"
        )
    elif (pointer == "pointer"):
        # Constant plus 5 are the temp register, vunerable af but who cares
        tempoffset = int(index) + 3
        set = (
            f"@{str(tempoffset)}\n"
            f"D=M\n"
        )
    elif (pointer == "static"):
        # Constant plus 5 are the temp register, vunerable af but who cares
        tempoffset = int(index) + 16
        set = (
            f"@{str(tempoffset)}\n"
            f"D=M\n"
        )

    else:
        # 1. Load value of index
        # 2. Set value of index to d
        # 3. Load the address that stores the address of the vms
        # 4. Set the address to addr of the vms
        # 5. Add the index offset and store to D and set the address

        #   Load the memory of the index to D

        # 6. Loads the stack pointer
        # 7. Sets the value of SP to the address
        # 8. Sets the top of the stack to the value of D

        # Reads the VMS and pushes it's value to the stack

        set = (
            f"@{index}\n"
            f"D=A\n"
            f"@{ps}\n"
            f"A=M\n"
            f"AD=D+A\n"

            f"D=M\n"

            f"@SP\n"
            f"A=M\n"
            f"M=D\n"
        )

    out = set + inc
    return out


def pop(pointer, index=0):
    ps = pointerhandler.pointer(pointer)
    if (pointer == "temp"):
        tempindex = int(index) + 5
        set = (
            f'@SP\n'            # Dec SP and load value into D
            f'D=M-1\n'
            f'M=D\n'
            f'A=D\n'
            f'D=M\n'

            f'@{tempindex}\n'     # Set the address of index + 5 to D ;/
            f'M=D\n'
        )
    elif (pointer == "pointer"):
        tempindex = int(index) + 3
        set = (
            f'@SP\n'            # Dec SP and load value into D
            f'D=M-1\n'
            f'M=D\n'
            f'A=D\n'
            f'D=M\n'

            f'@{tempindex}\n'     # Set the address of index + 5 to D ;/
            f'M=D\n'
        )
    elif (pointer == "static"):
        tempindex = int(index) + 16
        set = (
            f'@SP\n'            # Dec SP and load value into D
            f'D=M-1\n'
            f'M=D\n'
            f'A=D\n'
            f'D=M\n'

            f'@{tempindex}\n'     # Set the address of index + 5 to D ;/
            f'M=D\n'
        )

    else:
        # 1. Load SP
        # 2. Dec SP
        # 3. Set SP to Dec SP
        # 4. Set the address to the new sp
        # 5. Load the memory from the top of the stack into D

        # 6. Load R13
        # 7. Put the value of the poped stack into r13 memory

        # 8. Load value of index
        # 9. Set value of index to d
        # 10. Load the address that stores the address of the vms
        # 11. Set the address to addr of the vms
        # 12. Add the index offset and store to D and jump to it
        # 13. Load R14
        # 14. Store value of offset to R14

        # 15. Load R13
        # 16. Set Value of R13 to D
        # 17. Load R14
        # 18. Jump to the memory address stored in r14
        # 19. Set memory address of r 14 to d

        set = (

            f'@SP\n'
            f'D=M-1\n'
            f'M=D\n'
            f'A=D\n'
            f'D=M\n'

            f'@R13\n'
            f'M=D\n'

            f"@{index}\n"
            f"D=A\n"
            f"@{ps}\n"
            f"A=M\n"
            f"AD=D+A\n"
            f"@R14\n"
            f"M=D\n"

            f'@R13\n'
            f'D=M\n'
            f'@R14\n'
            f'A=M\n'
            f'M=D\n'

        )

    out = set
    return out
