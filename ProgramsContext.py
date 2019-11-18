from threading import Lock
REGISTERS_AMOUNT = 32


class ProgramsContext:
    """
    This class is a structure representation of the context of a program. It's
    mainly used to store the final values of the registers, as well as valuable
    information such as the ID, which core worked on the program, etc.
    """
    def __init__(self):
        self.lock = Lock() # lock to avoid conflicts between cores
        self.context_id = -1
        self.start_address = 0     # starting address from the instructions memory
        self.assigned_core = -1     # which core takes on the program
        self.taken = False      # flag to avoid core conflicts
        self.starting_clock_cycle = -1
        self.ending_clock_cycle = -1
        self.registers = [0] * REGISTERS_AMOUNT     # final results of the registers

    def print_registers(self):
        """
        Prints a user friendly state of the context of a program in order
        to check the values.
        :return:
        """
        print(self.registers)

