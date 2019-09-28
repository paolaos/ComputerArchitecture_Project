class ProgramContext:
    def __init__(self):
        self._context_id = -1
        self._start_address = 0
        self._assigned_core = -1
        self._taken = False
        self._starting_clock_cycle = -1
        self._ending_clock_cycle = -1
        self._registers = []

    @property
    def context_id(self):
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        self._context_id = context_id

    @property
    def start_address(self):
        return self._start_address

    @start_address.setter
    def start_address(self, start_address):
        self._start_address = start_address

    @property
    def assigned_core(self):
        return self._assigned_core

    @assigned_core.setter
    def assigned_core(self, assigned_core):
        self._assigned_core = assigned_core

    @property
    def taken(self):
        return self._taken

    @taken.setter
    def taken(self, taken):
        self._taken = taken

    @property
    def starting_clock_cycle(self):
        return self._starting_clock_cycle

    @starting_clock_cycle.setter
    def starting_clock_cycle(self, starting_clock_cycle):
        self._starting_clock_cycle = starting_clock_cycle

    @property
    def ending_clock_cycle(self):
        return self._ending_clock_cycle

    @ending_clock_cycle.setter
    def ending_clock_cycle(self, ending_clock_cycle):
        self._ending_clock_cycle = ending_clock_cycle

    @property
    def registers(self):
        return self._registers

    @registers.setter
    def registers(self, registers):
        self._registers = registers
