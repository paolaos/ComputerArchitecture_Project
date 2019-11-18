from Block import Block


class CacheLine:
    def __init__(self):
        self.status = False     # False = I, True = C
        self.block = Block()

    def get_block_id(self):
        """
        Get the block id of the block stored in a cache line
        :return: Current block id
        """
        return self.block.block_id

    def print_cache_line(self):
        """
        Print the contents of a cache line
        """
        status = "I"
        if self.status:
            status = "C"
        print(status, " ", self.block.block_id, " ", self.block.word_0, " ", self.block.word_1, " ", self.block.word_2,
              " ", self.block.word_3)
