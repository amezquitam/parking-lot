
class Space:

    def __init__(self, id: str, price: float, layer: int):
        self.__price = price
        self.__id = id
        self.__layer = layer


    @property
    def id(self): 
        return self.__id
    
    
    @property
    def price(self): 
        return self.__price
    
    
    @property
    def layer(self): 
        return self.__layer
