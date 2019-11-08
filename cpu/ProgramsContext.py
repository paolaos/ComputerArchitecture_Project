
REGISTERS_AMOUNT = 32


class ProgramsContext:
    def __init__(self):
        self.context_id = -1
        self.start_address = 0     # starting address from the instructions memory
        self.assigned_core = -1
        self.taken = False
        self.starting_clock_cycle = -1
        self.ending_clock_cycle = -1
        self.registers = [0] * REGISTERS_AMOUNT

    def print_registers(self):
        print(self.registers)
