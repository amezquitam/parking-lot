from Space import Space
from util import make_matrix


BYTECODE_A = 0x0041


def space_generator(row, col, size):
    # id generation. Note 0x0041 is 'A' in bytecode
    id = chr(BYTECODE_A + row) + str(col + 1)

    # layer represents "profundity"
    layer: int = min((row, col, size - row - 1, size - col - 1))
    price = calculate_price(size, layer)

    return Space(id, price, layer)


def calculate_price(size: int, layer: int):
    layer_counter = int(size / 2)
    return size * 1000 * (layer_counter - layer)


class ParkingLot:

    def __init__(self, size: int):
        self.__size = int(size)
        self.spaces = make_matrix(size, space_generator)
    
    
    @property
    def size(self):
        return self.__size
    

    @property
    def available_prices(self):
        return (calculate_price(self.size, layer) for layer in range(self.layer_count))

    @property
    def layer_count(self):
        return int(self.size / 2)