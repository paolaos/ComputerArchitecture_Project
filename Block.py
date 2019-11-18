class Block:
    def __init__(self):
        self.block_id = -1
        self.word_0 = []
        self.word_1 = []
        self.word_2 = []
        self.word_3 = []

    def get_block_id_from_address(self, address):
        """
        Determine the block number/id from a given address
        :param address: the address
        :return: Block id
        """
        return address // 16

    def get_word_from_number(self, number):
        word = number // 4
        if word == 0:
            return self.word_0
        if word == 1:
            return self.word_1
        if word == 2:
            return self.word_2
        if word == 3:
            return self.word_3
