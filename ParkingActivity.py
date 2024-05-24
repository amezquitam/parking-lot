
from datetime import datetime

class ParkingActivity:
    def __init__(self, v_plate: str, space_id: str, entry_time: datetime):
        self.__v_plate = v_plate
        self.__space_id = space_id
        self.__entry_time = entry_time
        self.__departure_time: datetime = None

    @property
    def v_plate(self):
        return self.__v_plate
    
    @property
    def space_id(self):
        return self.__space_id
    
    @property
    def entry_time(self):
        return self.__entry_time
    
    @property
    def departure_time(self):
        return self.__departure_time
    
    @property
    def active(self):
        return self.__departure_time == None

    @departure_time.setter
    def departure_time(self, departure_time: datetime):
        if departure_time < self.entry_time:
            raise ValueError('Departure time must be after entry time')
        self.__departure_time = departure_time