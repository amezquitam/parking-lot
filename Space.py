
class Space:

    def __init__(self, id: str, price: float):
        self._price = price
        self._id = id


    @property
    def id(self): 
        return self._id
    
    
    @property
    def price(self): 
        return self._price
