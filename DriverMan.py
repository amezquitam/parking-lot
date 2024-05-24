from datetime import date

class DriverMan:
    def __init__(self, id, name: str, dob: date, sex: str, preferred_layer) -> None:
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__sex = sex
        self.__preferred_layer = preferred_layer
    
    
    @property
    def name(self):
        return self.__name
    
    
    @property
    def sex(self):
        return self.__sex
    
    
    @property
    def dob(self):
        return self.__dob
    
    
    @property
    def preferred_layer(self):
        return self.__preferred_layer
    
    
    @property
    def id(self):
        return self.__id


    @property
    def age(self):
        today = date.today()
        age = today.year - self.dob.year
        if today.month < self.dob.month:
            age -= 1
        elif today.month == self.dob.month and today.day < self.dob.day:
            age -= 1
        return age
