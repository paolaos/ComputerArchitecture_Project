from threading import Thread, Barrier, BrokenBarrierError, active_count
from cpu.ProgramsContext import ProgramsContext
from cpu.Cache import Cache
from cpu.Instruction import Instruction
from cpu.Sync import Sync
import time

REGISTERS_AMOUNT = 32


class Core(Thread):
    def __init__(self, core_id, data_cache, instruction_cache, processor,
                 data_bus, instruction_bus, foreign_data_cache):
        Thread.__init__(self)
        self.core_id = core_id
        self.registers = [0] * REGISTERS_AMOUNT
        self.instructions_register = -1
        self.current_instruction = Instruction(-1, -1, -1, -1)

        self.processor = processor
        self.data_cache: Cache = data_cache
        self.instructions_cache: Cache = instruction_cache
        self.foreign_data_cache: Cache = foreign_data_cache
        self.pc = -1

        self.data_bus: Sync = data_bus
        self.instruction_bus: Sync = instruction_bus
        self.actual_program = ProgramsContext()
        self.waiting_cycles = 0

    def decode_instruction(self):
        instruction_number = self.current_instruction.code

        if instruction_number == 19:
            # addi
            x = self.registers[self.current_instruction.op2]
            n = self.current_instruction.op3
            self.registers[self.current_instruction.op1] = x + n
            self.pc += 4

        if instruction_number == 71:
            # add
            x = self.registers[self.current_instruction.op2]
            n = self.registers[self.current_instruction.op3]
            self.registers[self.current_instruction.op1] = x + n
            self.pc += 4

        if instruction_number == 83:
            # sub
            x = self.registers[self.current_instruction.op2]
            n = self.registers[self.current_instruction.op3]
            self.registers[self.current_instruction.op1] = x - n
            self.pc += 4

        if instruction_number == 72:
            # mul
            x = self.registers[self.current_instruction.op2]
            n = self.registers[self.current_instruction.op3]
            self.registers[self.current_instruction.op1] = x * n
            self.pc += 4

        if instruction_number == 56:
            # div
            x = self.registers[self.current_instruction.op2]
            n = self.registers[self.current_instruction.op3]
            self.registers[self.current_instruction.op1] = x // n
            self.pc += 4

        if instruction_number == 5:
            # load
            register = self.current_instruction.op1
            n = self.current_instruction.op3 + self.registers[self.current_instruction.op2]
            required_cycles = self.data_cache.get_loading_cycles(n)
            if required_cycles == 0:
                # doesn't need the bus because it's a hit
                self.registers[register] = self.data_cache.get_word_from_address(n)
                self.waiting_cycles = 0
                self.pc += 4
            elif required_cycles > 0 and self.data_bus.get_resource(required_cycles, self.core_id):
                # need the bus because it's a miss
                self.waiting_cycles = required_cycles
                self.registers[register] = self.data_cache.get_word_from_address(n)
                self.pc += 4

        if instruction_number == 37:
            # store
            register = self.current_instruction.op2
            n = self.current_instruction.op3
            address = n + self.registers[self.current_instruction.op1]
            required_cycles = 6
            if self.data_bus.get_resource(required_cycles, self.core_id):
                # if the bus is available
                # invalidate block in the other cache
                self.waiting_cycles = required_cycles
                self.foreign_data_cache.invalidate_block(address)
                # store data
                self.data_cache.store_word(self.registers[register], address)
                self.pc += 4

        if instruction_number == 99:
            # Branch eq
            x1 = self.registers[self.current_instruction.op1]
            x2 = self.registers[self.current_instruction.op2]
            if x1 == x2:
                self.pc += 4 * self.current_instruction.op3
            else:
                self.pc += 4

        if instruction_number == 100:
            # Branch ne
            x1 = self.registers[self.current_instruction.op1]
            x2 = self.registers[self.current_instruction.op2]
            if x1 != x2:
                self.pc += 4 * self.current_instruction.op3
            else:
                self.pc += 4

        if instruction_number == 111:
            # jal
            self.registers[self.current_instruction.op1] = self.pc
            self.pc = self.pc + self.current_instruction.op2
            # todo check this

        if instruction_number == 103:
            # jalr
            self.registers[self.current_instruction.op1] = self.pc
            self.pc = self.current_instruction.op2 + self.current_instruction.op3

        if instruction_number == 999:
            # Save ending registers
            i = 0
            while i < len(self.registers):
                self.actual_program.registers[i] = self.registers[i]
                i += 1
            self.actual_program.ending_clock_cycle = self.processor.clock.get_clock()
            print('Program', self.actual_program.context_id, 'ended.')

            # Get next program to run it
            self.actual_program: ProgramsContext = self.processor.get_next_program()
            self.actual_program.assigned_core = self.core_id
            self.actual_program.taken = True
            self.actual_program.starting_clock_cycle = self.processor.clock.get_clock()
            self.pc = self.actual_program.start_address
            self.reset_registers()

    def run(self):
        self.actual_program = self.processor.get_next_program()
        self.actual_program.assigned_core = self.core_id
        self.actual_program.taken = True
        self.pc = self.actual_program.start_address
        self.actual_program.starting_clock_cycle = self.processor.clock.get_clock()
        while self.actual_program.context_id != -1:
            # set current instruction
            self.current_instruction = self.instructions_cache.get_word_from_address(self.pc)
            if self.waiting_cycles == 0:
                self.decode_instruction()
            if self.waiting_cycles > 0 and self.data_bus.core_id == self.core_id:
                self.waiting_cycles -= 1
                self.data_bus.decrease_cycles()
            self.processor.clock.wait_for_next_cycle()

        self.processor.clock.remove_thread()

        while self.processor.clock.thread_count > 0:
            self.processor.clock.wait_for_next_cycle()
        return 0

    def reset_registers(self):
        i = 0
        while i < len(self.registers):
            self.registers[i] = 0
            i += 1
