from threading import Thread
from cpu.ProgramsContextHelper import get_next_pending_program, save_context
from cpu.ProgramsContext import ProgramsContext
from cpu.Cache import Cache
from cpu.Instruction import Instruction

REGISTERS_AMOUNT = 32


class Core(Thread):
    def __init__(self, core_id, data_cache, instruction_cache, processor, data_bus, instruction_bus):
        Thread.__init__(self)
        self.core_id = core_id
        self.registers = [0] * REGISTERS_AMOUNT
        self.instructions_register = -1
        self.current_instruction = Instruction(-1, -1, -1, -1)

        self.processor = processor
        self.data_cache: Cache = data_cache
        self.instructions_cache = instruction_cache
        self.pc = -1

        self.data_bus = data_bus
        self.instruction_bus = instruction_bus
        self.actual_program = ProgramsContext()

    def decode_instruction(self):
        instruction_number = self.current_instruction.code

        if instruction_number == 19:
            print('addi')
            x = self.registers[self.current_instruction.op2]
            n = self.current_instruction.op3
            self.registers[self.current_instruction.op1] = x + n

        if instruction_number == 71:
            print('add')
            x = self.registers[self.current_instruction.op2]
            n = self.registers[self.current_instruction.op3]
            self.registers[self.current_instruction.op1] = x + n

        if instruction_number == 83:
            print('sub')
            x = self.registers[self.current_instruction.op2]
            n = self.registers[self.current_instruction.op3]
            self.registers[self.current_instruction.op1] = x - n

        if instruction_number == 72:
            print('mul')
            x = self.registers[self.current_instruction.op2]
            n = self.registers[self.current_instruction.op3]
            self.registers[self.current_instruction.op1] = x * n

        if instruction_number == 56:
            print('div')
            x = self.registers[self.current_instruction.op2]
            n = self.registers[self.current_instruction.op3]
            self.registers[self.current_instruction.op1] = x // n

        if instruction_number == 5:
            print('Load instruction')

        if instruction_number == 37:
            print('Store instruction')

        if instruction_number == 99:
            print('Branch eq')

        if instruction_number == 100:
            print('Branch ne')

        if instruction_number == 111:
            print('jal')

        if instruction_number == 103:
            print('jalr')

        if instruction_number == 999:
            # Save ending registers
            self.actual_program.registers = self.registers
            # TODO save clock
            print('Program', self.actual_program.context_id, 'ended.')

            # Get next program to run it
            self.actual_program: ProgramsContext = get_next_pending_program(self.processor.contexts)
            self.actual_program.assigned_core = self.core_id
            self.actual_program.taken = True
            # TODO save starting clock
            self.pc = self.actual_program.start_address

    def run(self):
        self.actual_program = get_next_pending_program(self.processor.contexts)
        self.actual_program.assigned_core = self.core_id
        self.actual_program.taken = True
        self.pc = self.actual_program.start_address
        # TODO save starting clock
        while self.actual_program.context_id != -1:
            # set current instruction
            self.current_instruction = self.instructions_cache.get_word_from_address(self.pc)
            self.pc += 4
            self.decode_instruction()

        return 0

    def reset_registers(self):
        i = 0
        while i < REGISTERS_AMOUNT:
            self.registers[i] = 0
            i += 1
