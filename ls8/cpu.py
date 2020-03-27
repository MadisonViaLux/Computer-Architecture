"""CPU functionality."""

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
#     new_line = int(line[:8], 2)
#     print(new_line)

# print(hex(0b00001111))

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.pc = 0
        self.reg = [0] * 8
        self.flag = 0b00000000
        # self.E = 0
        # self.L = 0
        # self.G = 0

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        file = open("examples/sctest.ls8", "rb")

        for instruction in file:
            new_line = int(instruction[:8], 2)
            # print("new_line:", new_line, "\n")
            self.ram[address] = new_line
            address += 1

    # def alu(self, op, reg_a, reg_b):
    #     """ALU operations."""
    #
    #     if op == "ADD":
    #         self.reg[reg_a] += self.reg[reg_b]
    #     elif op == "SUB":
    #         self.reg[reg_a] -= self.reg[reg_b]
    #     else:
    #         raise Exception("Unsupported ALU operation")

    # def trace(self):
    #     """
    #     Handy function to print out the CPU state. You might want to call this
    #     from run() if you need help debugging.
    #     """
    #
    #     print(f"TRACE: %02X | %02X %02X %02X |" % (
    #         self.pc,
    #         #self.fl,
    #         #self.ie,
    #         self.ram_read(self.pc),
    #         self.ram_read(self.pc + 1),
    #         self.ram_read(self.pc + 2)
    #     ), end='')
    #
    #     for i in range(8):
    #         print(" %02X" % self.reg[i], end='')
    #
    #     print()


    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value

    def MUL(self, valA, valB):
        self.ram[valA] = self.ram[valA] * self.ram[valB]

    # def CMP(self, valA, valB):
    #     if valA == valB:
    #         self.E = 1
    #     elif valA < valB:
    #         self.L = 1
    #     elif valA > valB:
    #         self.G = 1
    #     print("E__L__G: ***", self.E, self.L, self.G)

    def CMP(self, regA, regB):
        if self.reg[regA] == self.reg[regB]:
            self.flag = 0b00000001
        elif self.reg[regA] > self.reg[regB]:
            self.flag = 0b00000010
        else:
            self.flag = 0b00000100

    # def JEQ(self, valeE):
    #     if valeE == 1:
    #         self.pc = valeE
    #     else:
    #         self.pc += 2
    #
    # def JNE(self, valeE):
    #     if valeE == 0:
    #         self.pc = valeE
    #     else:
    #         self.pc += 2


    def run(self):
        """Run the CPU."""
        running = True

        while running:

            if self.ram[self.pc] == 0b10000010: #LDI = "set this register to this value"
                self.ram_write(self.ram_read(self.pc + 1), self.ram_read(self.pc + 2))
                self.pc += 3

            elif self.ram[self.pc] == 0b01000111: #PRN = prints pseudo-instruction
                print(self.ram_read(self.ram[self.pc + 1]))
                self.pc += 2

            elif self.ram[self.pc] == 0b10100010: #MUL
                self.MUL(self.ram_read(self.pc + 1), self.ram_read(self.pc + 2))
                self.pc += 3

            elif self.ram[self.pc] == 0b10100111: #CMP
                self.CMP(self.ram_read(self.pc + 1), self.ram_read(self.pc + 2))
                self.pc += 3

            elif self.ram[self.pc] == 0b01010101: #JEQ
                if self.flag == 0b00000001:
                    self.pc = self.reg[self.ram_read(self.pc + 1)]
                else:
                    self.pc += 2

            elif self.ram[self.pc] == 0b01010110: #JNE
                if self.flag != 0b00000001:
                    self.pc = self.reg[self.ram_read(self.pc + 1)]
                else:
                    self.pc += 2

            elif self.ram[self.pc] == 0b01010100: #JMP
                self.pc = self.reg[self.ram_read(self.pc + 1)]

            elif self.ram[self.pc] == 0b00000001: #HLT = halt the CPU
                self.pc = 0
                running = False

            else:
                print(f"Unknown instruction at pc point (or line): {self.pc + 1}")
                sys.exit(1)




