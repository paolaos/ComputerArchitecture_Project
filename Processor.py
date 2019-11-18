from Memory import Memory
from Core import Core
from Sync import Sync
from Cache import Cache
from ProgramsContextHelper import create_context
from ProgramsContext import ProgramsContext
from Clock import Clock
from threading import Lock
import os

# required clock cycles
LOAD_INSTRUCTION_TO_CACHE = 10
LOAD_DATA_TO_CACHE = 20
WRITE_A_WORD = 5
INVALIDATE_BLOCK = 1


class Processor:
    def __init__(self):
        self.data_bus = Sync()
        self.instruction_bus = Sync()
        self.data_memory = Memory(0, 380)
        self.instructions_memory = Memory(24, 636)
        self.memory = Memory(0, 1024)
        self.threads = 2
        self.clock = Clock()

        self.core_1_data_cache = Cache(self.memory, LOAD_DATA_TO_CACHE)
        self.core_1_instruction_cache = Cache(self.memory, LOAD_INSTRUCTION_TO_CACHE)
        self.core_2_instruction_cache = Cache(self.memory, LOAD_INSTRUCTION_TO_CACHE)
        self.core_2_data_cache = Cache(self.memory, LOAD_DATA_TO_CACHE)

        self.core_1 = Core(1, self.core_1_data_cache, self.core_1_instruction_cache, self, self.data_bus,
                           self.instruction_bus, self.core_2_data_cache)
        self.core_2 = Core(2, self.core_2_data_cache, self.core_2_instruction_cache, self, self.data_bus,
                           self.instruction_bus, self.core_1_data_cache)

        self.contexts = []
        self.context_lock = Lock()

    # Processor methods
    def kick_start_program(self):
        """
        Do the necessary things to start the simulation: Load the programs in memory and start the threads
        :return:
        """
        self.load_memory_instructions()
        self.core_1.start()
        self.core_2.start()
        self.core_1.join()
        self.core_2.join()
        self.print_final_execution_results()

    def get_next_program(self):
        """
        Get the next program (hilillo) that is pending to run
        :return: Program context of the next program to run
        """
        program: ProgramsContext = ProgramsContext()
        tries = 0
        with self.context_lock:
            while program.context_id == -1 and tries < len(self.contexts):
                if not self.contexts[tries].taken:
                    program = self.contexts[tries]
                tries += 1

            program.taken = True
        return program

    def load_memory_instructions(self):
        """
        Opens the files from the assets folder and stores the instructions of each program
        """
        current_file_number = 0
        current_address = 384
        for file_name in os.listdir('./assets'):
            file_ = open('./assets/' + file_name, 'r')
            create_context(current_file_number, current_address, self.contexts)
            current_address = self.store_instructions_in_memory(file_, current_address, file_name)
            print("Uploaded ", file_name, "as program ", current_file_number)
            current_file_number += 1
        print("The memory was successfully loaded with", current_file_number, "file(s)")

    def store_instructions_in_memory(self, file_, current_address, file_name):
        """"
        Saves the files content in the memory starting in the current address
        :param file_: file with the code
        :param current_address: the next free address on the memory
        :param file_name: name of the file
        :return: the next available address in the memory
        """
        line = file_.readline()
        while line:
            split_line = line.split()   # instruction as a list of string
            for i in split_line:
                if current_address >= self.memory.length:
                    print("The instruction memory is full, there was an error uploading ", file_name)
                    break
                self.memory.memory[current_address] = int(i)
                current_address += 1

            line = file_.readline()

        return current_address

    def print_final_execution_results(self):
        """
        Print the final execution results from the simulation
        """
        print("-------------EXECUTION RESULTS-------------")
        print("Total execution cycles: ", self.clock.get_clock())
        print("Data memory:")
        self.memory.print_part_of_memory(0, 380)
        print("Data caches:")
        print("Core 1:")
        self.core_1.data_cache.print_cache()
        print("Core 2:")
        self.core_2.data_cache.print_cache()
        print("Program's results:")
        for program in self.contexts:
            print("Program", program.context_id, "was executed by core", program.assigned_core)
            print("Execution clock cycles: ", program.ending_clock_cycle - program.starting_clock_cycle)
            print("Final registers:")
            program.print_registers()
            print()
