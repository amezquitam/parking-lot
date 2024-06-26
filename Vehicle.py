
from datetime import date

class Vehicle:
    def __init__(self, plate: str, mark: str, year: int, owner_id: str):
        self.__plate = plate
        self.__mark = mark
        self.__year = year
        self.__owner_id = owner_id
    

    @property
    def plate(self):
        return self.__plate
    
    
    @property
    def mark(self):
        return self.__mark
    
    
    @property
    def year(self):
        return self.__year
    
    
    @property
    def owner_id(self):
        return self.__owner_id


    @property
    def age(self):
        today = date.today()
        return today.year - self.year
