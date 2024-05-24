
class Space:

    def __init__(self, id: str, price: float):
        self.__price = price
        self.__id = id


    @property
    def id(self): 
        return self.__id
    
    
    @property
    def price(self): 
        return self.__price
