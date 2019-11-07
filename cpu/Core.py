from cpu.Cache import Cache
from cpu.Block import Block
import threading
from cpu.ProgramsContext import ProgramsContext
from functools import partial

REGISTERS_AMOUNT = 32


class Core:
    def __init__(self, data_cache, instruction_cache):
        self._registers = [0] * REGISTERS_AMOUNT
        self._instructions_register = -1
        self._current_instruction = []

        self.my_data = threading.local()
        self.my_data.data_cache = data_cache
        self.my_data.instructions_cache = instruction_cache

    @property
    def registers(self):
        return self._registers

    @registers.setter
    def registers(self, registers):
        self._registers = registers

    @property
    def instructions_register(self):
        return self._instructions_register

    @instructions_register.setter
    def instructions_register(self, instructions_register):
        self._instructions_register = instructions_register

    @property
    def current_instruction(self):
        return self._current_instruction

    @current_instruction.setter
    def current_instruction(self, current_instruction):
        self._current_instruction = current_instruction

    @property
    def data_cache(self):
        return self._data_cache

    @data_cache.setter
    def data_cache(self, data_cache):
        self._data_cache = data_cache

    @property
    def instructions_cache(self):
        return self._instructions_cache

    @instructions_cache.setter
    def instructions_cache(self, instructions_cache):
        self._instructions_cache = instructions_cache

    def run_program(self, program_context):
        print('todo')

    def decode_instructions(self, block):
        instruction_number = block[0]

        def addi():
            block[0] = block[1] + block[2]
            return block

        def add():
            return 0

        def sub():
            return 0

        def mul():
            return 0

        def div():
            return 0


        switcher = {
            19: addi,
            71: add,
            83: sub,
            72: mul,
            56: div,
            5: 'lw',
            37: 'sw',
            99: 'beq',
            100: 'bne',
            111: 'jal',
            103: 'jalr',
            999: 'END'

        }

        instruction = switcher.get(instruction_number, lambda: "Instruction does not exist")
        return instruction()



