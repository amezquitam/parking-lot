
from datetime import date

class Vehicle:
    def __init__(self, plate, mark, year):
        self.__plate = plate
        self.__mark = mark
        self.__year = year
    

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
    def age(self):
        today = date.today()
        return today.year - self.year
