from Space import Space
from util import make_matrix


BYTECODE_A = 0x0041


def space_generator(row, col, size):
    # id generation. Note 0x0041 is 'A' in bytecode
    id = chr(BYTECODE_A + row) + str(col)

    # layer represents "profundity"
    layer_counter = int(size / 2)
    for layer in range(layer_counter):
        first = layer
        last = size - layer - 1
        if row == first or col == first or row == last or col == last:
            price = size * 1000 * (layer_counter - layer)
    
    return Space(id, price)


class ParkingLot:

    def __init__(self, size: int):
        self.__rows = self.__cols = size
        self.spaces = make_matrix(size, space_generator)
    
    
    @property
    def rows(self):
        return self.__rows
    

    @property
    def cols(self):
        return self.__cols
        
    