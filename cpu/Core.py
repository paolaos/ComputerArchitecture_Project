from cpu.Cache import Cache


class Core:
    def __init__(self):
        self._registers = []
        self._instructions_register = -1
        self._current_instruction = []
        self._data_cache = Cache()
        self._instructions_cache = Cache()

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
