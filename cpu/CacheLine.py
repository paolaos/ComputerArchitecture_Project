from cpu.Block import Block


class CacheLine:
    def __init__(self):
        self._status = False
        self._block = Block()

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def block(self):
        return self._block

    @block.setter
    def block(self, block):
        self._block = block

    def get_block_id(self):
        return self.block.block_id
