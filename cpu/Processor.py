from cpu.Memory import Memory
from cpu.Core import Core
from cpu.Sync import Sync
from cpu.Cache import Cache
from cpu.ProgramsContextHelper import create_context
import os


class Processor:
    def __init__(self):
        self.clock = 0
        self.data_bus = Sync()
        self.instruction_bus = Sync()
        self.data_memory = Memory(0, 380)
        self.instructions_memory = Memory(24, 636)
        self.memory = Memory(0, 1024)

        self.core_1_data_cache = Cache(self.memory)
        self.core_1_instruction_cache = Cache(self.memory)
        self.core_2_instruction_cache = Cache(self.memory)
        self.core_2_data_cache = Cache(self.memory)
        self.core_1 = Core(1, self.core_1_data_cache, self.core_1_instruction_cache, self, self.data_bus,
                           self.instruction_bus)
        self.core_2 = Core(2, self.core_2_data_cache, self.core_2_instruction_cache, self, self.data_bus,
                           self.instruction_bus)

        self.contexts = []

    # Processor methods
    def kick_start_program(self):
        self.load_memory_instructions()
        self.core_1.run()
        self.core_2.run()
        self.print_final_program_context()
        # todo add ending of the program

    def load_memory_instructions(self):
        current_file_number = 0
        current_address = 384
        for file_name in os.listdir('../assets'):
            file_ = open('../assets/' + file_name, 'r')
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

    def print_final_program_context(self):
        print("Program's results:")
        for program in self.contexts:
            print("Program", program.context_id, "was executed by core", program.assigned_core)
            print("Final registers:")
            program.print_registers()