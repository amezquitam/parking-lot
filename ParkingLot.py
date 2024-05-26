from Space import Space
from util import make_matrix


def space_generator(row, col, size):
    # id generation. Note 0x0041 is 'A' in bytecode
    letters = 'ABCDEFGHIJ'
    id = letters[row] + str(col + 1)

    # layer represents "profundity". 0 means just at matrix border
    layer: int = min((row, col, size - row - 1, size - col - 1))
    price = calculate_price(size, layer)

    return Space(id, price, layer)


def calculate_price(size: int, layer: int):
    price_map = {
        6: [10000, 8000, 6000],
        8: [32000, 24000, 16000, 8000],
        10: [50000, 40000, 30000, 20000, 10000]
    }
    
    return price_map[size][layer]


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
