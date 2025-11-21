'''
"opcode rD rA rB" 또는 "opcode rD rA #C"
레지스터 rA와 rB에 있는 두 수 || 레지스터 rA에 있는 수와 상수 #C를 opcode에 해당하는 연산을 수행
그 결괏값을 레지스터 rD에 저장하는 명령어
rA는 opcode에 따라 사용하지 않을 수도 있다
opcode, rD, rA, rB, #C를 각 bit의 자리에 맞게 2진수 0과 1로 이루어진 16-bit 기계어 코드로 변역

0~4 : CPU가 수행해야 할 연산을 나타내는 opcode이다. 만약 4번 bit가 0일 경우 레지스터 rB를, 1일 경우 상수 #C를 사용한다.
5 : 사용하지 않는 bit이며, 항상 0이다.
6~8 : 결괏값을 저장하는 레지스터 rD의 번호이다.
9~11 : 연산에 사용되는 레지스터 rA의 번호이다. 사용하지 않을 경우에는 000이다.
12~15 : 만약 4번 bit가 0일 경우 12~14번 bit는 연산에 사용되는 레지스터 rB의 번호이며, 15번 bit는 항상 0이다. 만약 4번 bit가 1일 경우 12~15번 bit는 상수 #C이다.

N개의 각 줄에는
"opcode rD rA rB" 또는 "opcode rD rA #C"

opcode       rD   rA  rB
MOVC          1   0   5
00101   0    001 000 0101

'''

n = int(input())
command = {
    "ADD": "0000",
    "SUB": "0001",
    "MOV": "0010",
    "AND": "0011",
    "OR": "0100",
    "NOT": "0101",
    "MULT": "0110",
    "LSFTL": "0111",
    "LSFTR": "1000",
    "ASFTR": "1001",
    "RL": "1010",
    "RR": "1011"
}
for _ in range(n):
    temp = list(input().split())
    com =''
    checkC = False
    if temp[0][-1] == "C":
        com +=command[temp[0][:-1]]+"10"
        checkC = True
    else:
        com+=command[temp[0]]+"00"
    com+=format(int(temp[1]),'03b')
    com+=format(int(temp[2]),'03b')
    if checkC:
        com += format(int(temp[3]), '04b')
        
    else:
        com += format(int(temp[3]), '03b') +"0"
    print(com)

