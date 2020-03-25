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

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.pc = 0

    def load(self, file):
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

        # file = open("examples/mult.ls8", "rb")

        with open("examples/mult.ls8", "rb") as txtfile:
            mytextstring = txtfile.read()

        binarray = ' '.join(format(ch, 'b') for ch in bytearray(mytextstring))

        print(binarray)

        # for instruction in file:
        #     print(instruction)
        #     self.ram[address] = instruction
        #     address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "SUB":
            self.reg[reg_a] -= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()


    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value


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

            elif self.ram[self.pc] == 0b00000001: #HLT = halt the CPU
                self.pc = 0
                running = False




