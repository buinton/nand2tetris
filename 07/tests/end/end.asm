//push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 53
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
//add
@SP
D=M-1
M=D
A=D
D=M
@R13
M=D
@SP
D=M-1
M=D
A=D
D=M
@R13
D=D+M
@SP
A=M
M=D
@SP
M=M+1
//push constant 112
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub
@SP
D=M-1
M=D
A=D
D=M
@R13
M=D
@SP
D=M-1
M=D
A=D
D=M
@R13
D=D-M
@SP
A=M
M=D
@SP
M=M+1
//neg
@SP
D=M-1
M=D
A=D
D=-M
@SP
A=M
M=D
@SP
M=M+1
//and
@SP
D=M-1
M=D
A=D
D=M
@R13
M=D
@SP
D=M-1
M=D
A=D
D=M
@R13
D=D&M
@SP
A=M
M=D
@SP
M=M+1
//push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
//or
@SP
D=M-1
M=D
A=D
D=M
@R13
M=D
@SP
D=M-1
M=D
A=D
D=M
@R13
D=D|M
@SP
A=M
M=D
@SP
M=M+1
//not
@SP
D=M-1
M=D
A=D
D=!M
@SP
A=M
M=D
@SP
M=M+1