import sys




# 10000010 # LDI R0,8
# 00000000
# 00001000
# 10000010 # LDI R1,9
# 00000001
# 00001001
# 10100010 # MUL R0,R1
# 00000000
# 00000001
# 01000111 # PRN R0
# 00000000
# 00000001 # HLT

# file = open("examples/mult.ls8", "rb")
#
# for line in file:
#     print(line)




# file = open("examples/mult.ls8", "rb")

# with open("examples/mult.ls8", "r") as txtfile:
#     mytextstring = txtfile.read()
#
# binarray = ' '.join(format(ch, 'b') for ch in bytearray(mytextstring))
#
# print(binarray)



PRINT_BEEJ     = 1
HALT           = 2
PRINT_NUM      = 3
SAVE           = 4  # Save a value to a register
PRINT_REGISTER = 5  # Print a value from a register
ADD            = 6  # regA += regB

memory = [
  PRINT_BEEJ,
  SAVE,
  65,
  2,
  SAVE,
  20,
  3,
  ADD,
  2,
  3,
  PRINT_REGISTER,
  2,
  HALT
]

register = [0] * 8

pc = 0
running = True

while running:
    command = memory[pc]

    if command == PRINT_BEEJ:
        print("Beej!")
        pc += 1

    elif command == HALT:
        running = False
        pc += 1

    elif command == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        pc += 2

    elif command == SAVE:
        num = memory[pc + 1]
        reg = memory[pc + 2]
        register[reg] = num
        pc += 3

    elif command == PRINT_REGISTER:
        reg = memory[pc + 1]
        print(register[reg])
        pc += 2

    elif command == ADD:
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] += register[reg_b]
        pc += 3

    else:
        print(f"Unknown instruction: {command}")
        sys.exit(1)




yo = int("100110", 2)

print(yo)


#___________________________________________________________________________________

# 2 ** 0 = 1
# 2 ** 1 = 2
# 2 ** 2 = 4
# 2 ** 3 = 8
# 2 ** 4 = 16
# 2 ** 5 = 32
# 2 ** 6 = 64
# 2 ** 7 = 128
# 2 ** 8 = 256
# 2 ** 9 = 512
# 2 ** 10 = 1024

# 0b10100110

# 0 - 0
# 1 - 2
# 1 - 4
# 0 - 0
# 0 - 0
# 1 - 32
# 0 - 0
# 1 - 128


# 123


# 10 ** 0 = 1
# 10 ** 1 = 10
# 10 ** 2 = 100

# 3 - 3
# 2 - 20
# 1 - 100

# 123



# 0b 0011 0101 = 53

# 0x35

# 0b11001011 = 0xCB = 203

# 1  - 11 * 1
# 16 - 12 * 16

# 11 + 64 + 128

# 0b11111111 = 0xFF = 255

# 0b1111

# 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F




# A and B
# A     B     result
# -------------------
# 0     0       0
# 0     1       0
# 1     0       0
# 1     1       1


# A or B
# A     B     result
# -------------------
# 0     0       0
# 0     1       1
# 1     0       1
# 1     1       1


# A xor B
# A     B     result
# -------------------
# 0     0       0
# 0     1       1
# 1     0       1
# 1     1       0


# A and not B
# A     B  not B   result
# -------------------
# 0     0    1       0
# 0     1    0       0
# 1     0    1       1
# 1     1    0       0


# not (A and B) or B and (not A and B)

# not (A and B) <-> (not A or not B)
# A     B     result
# -------------------
# 0     0       1
# 0     1       1
# 1     0       1
# 1     1       0


# for A in [False, True]:
#     for B in [False, True]:
#         print(f"{A} - {B} -- {(not A or not B)}")



#     111
#   01010101
# + 10011100
# ----------
#   11110001


# 64 * 18


# A + B
# A     B    carry  sum
# ---------------------
# 0     0      0     0
# 0     1      0     1
# 1     0      0     1
# 1     1      1     0


# A and B
# A     B     result
# -------------------
# 0     0       0
# 0     1       0
# 1     0       0
# 1     1       1


# 4 & 3 = 0

#   0100
# & 0011
# -------
#   0000


# A or B
# A     B     result
# -------------------
# 0     0       0
# 0     1       1
# 1     0       1
# 1     1       1


# 14 | 6 = ?
#   1110
# | 0110
# ------
#   1110


# 0b10101010

# 0b11110000

#   01011000
# | 00000100
# -----------
#   01011100

#   01011100

# 01011000 >> 4
# 00101100
# 00010110
# 00001011
# 00000101


# 01011000 << 2
# 10110000
# 01100000
