from threading import Thread, local
from cpu.ProgramsContextHelper import get_next_pending_program, save_context
from cpu.ProgramsContext import ProgramsContext
from cpu.Cache import Cache
from cpu.Processor import Processor

REGISTERS_AMOUNT = 32


class Core(Thread):
    def __init__(self, core_id, data_cache, instruction_cache, processor, data_bus, instruction_bus):
        Thread.__init__(self)
        self.core_id = core_id
        self._registers = [0] * REGISTERS_AMOUNT
        self._instructions_register = -1
        self._current_instruction = []

        self.processor: Processor = processor
        self.data_cache: Cache = data_cache
        self.instructions_cache = instruction_cache
        self.pc = -1

        self.data_bus = data_bus
        self.instruction_bus = instruction_bus
        self.actual_program: ProgramsContext = None

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

    def decode_instruction(self):
        instruction_number = self.current_instruction[0]

        def addi():
            x = self.registers[self.current_instruction[2]]
            n = self.current_instruction[3]
            self.registers[self.current_instruction[1]] = x + n

        def add():
            x = self.registers[self.current_instruction[2]]
            n = self.registers[self.current_instruction[3]]
            self.registers[self.current_instruction[1]] = x + n

        def sub():
            x = self.registers[self.current_instruction[2]]
            n = self.registers[self.current_instruction[3]]
            self.registers[self.current_instruction[1]] = x - n

        def mul():
            x = self.registers[self.current_instruction[2]]
            n = self.registers[self.current_instruction[3]]
            self.registers[self.current_instruction[1]] = x * n

        def div():
            x = self.registers[self.current_instruction[2]]
            n = self.registers[self.current_instruction[3]]
            self.registers[self.current_instruction[1]] = x // n

        def lw():
            print('Load instruction')

        def sw():
            print('Store instruction')

        def beq():
            print('Branch eq')

        def bne():
            print('Branch ne')

        def jal():
            print('jal')

        def jalr():
            print('jalr')

        def end():
            # Save ending registers
            self.actual_program.registers = self.registers
            # TODO save clock
            save_context(self.actual_program, self.processor.contexts)
            # Get next program to run it
            self.actual_program: ProgramsContext = get_next_pending_program(self.processor.contexts)
            self.actual_program.assigned_core = id
            # TODO save starting clock
            print('end program')

        switcher = {
            19: addi,
            71: add,
            83: sub,
            72: mul,
            56: div,
            5: lw,
            37: sw,
            99: beq,
            100: bne,
            111: jal,
            103: jalr,
            999: end

        }

        instruction = switcher.get(instruction_number, lambda: "Instruction does not exist")
        return instruction()

    def run(self):
        self.actual_program: ProgramsContext = get_next_pending_program(self.processor.contexts)
        self.actual_program.assigned_core = id
        # TODO save starting clock
        while self.actual_program is not None:
            print('Running program.')
            self.pc = self.actual_program.start_address
            # set current instruction
            self.current_instruction = self.instructions_cache.get_word_from_address(self.pc)

            self.decode_instruction()

        return 0
