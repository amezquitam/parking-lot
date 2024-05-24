from DriverMan import DriverMan
from Vehicle import Vehicle
from ParkingLot import ParkingLot
from ParkingActivity import ParkingActivity

from datetime import datetime
from typing import TypeVar, Callable


T = TypeVar('T')


def contains(iter: list[T], func: Callable[[T], bool]) -> bool:
    return len(list(filter(func, iter))) > 0


def find(iter: list[T], func: Callable[[T], bool]):
    encountered = list(filter(func, iter))
    if len(encountered) > 0:
        return encountered[0]
    else: 
        return None


class DriverManager:
    driver_man_list: list[DriverMan] = []

    def add(self, driver: DriverMan):
        if self.contains(driver.id):
            raise ValueError("driver already registered")
        if driver.age < 18:
            raise ValueError("driver age must be at least 18")
        
    def contains(self, id: str):
        return contains(self.driver_man_list, lambda driver: driver.id == id)
    
    def find(self, id: str):
        return find(self.driver_man_list, lambda driver: driver.id == id)


class VehicleManager:
    vehicle_list: list[Vehicle] = []

    def add(self, vehicle: Vehicle):
        if self.contains(vehicle.plate):
            raise ValueError("vehicle already registered")
        
        if vehicle.age > 10:
            raise ValueError("vehicle must less than 10 years old")

    def contains(self, plate: str):
        return contains(self.vehicle_list, lambda vehicle: vehicle.plate == plate)
    
    def find(self, plate: str):
        return find(self.vehicle_list, lambda vehicle: vehicle.plate == plate)


class ParkingManager:
    
    def __init__(self, size: int):
        self.__parking = ParkingLot(size)
        self.__parking_activity: list[ParkingActivity] = []

    
    def free_spaces_matrix(self):
        return [[self.is_occupied(space.id) for space in column] for column in self.parking.spaces]


    def assign_space_to_vehicle(self, vehicle_plate: str, driver_preferred_layer: int, entry_time: datetime):
        if self.is_parked(vehicle_plate):
            raise ValueError(f"Vehicle with plate {vehicle_plate} is already parked")

        space = self.find_next_free_space_with_layer(driver_preferred_layer)

        new_parking_activity = ParkingActivity(vehicle_plate, space.id, entry_time)

        self.parking_activity.append(new_parking_activity)

    
    def find_next_free_space_with_layer(self, driver_preferred_layer: int):
        for column in self.parking.spaces:
            for space in column:
                if space.layer != driver_preferred_layer:
                    continue
                    
                if self.is_occupied(space.id):
                    continue
                
                return space


    def is_occupied(self, space_id: str):
        space = find(self.parking_activity, lambda pa: pa.active and pa.space_id == space_id)
        return space != None
    
    def is_parked(self, vehicle_plate):
        space = find(self.parking_activity, lambda pa: pa.active and pa.v_plate == vehicle_plate)
        return space != None
    
    def take_out_vehicle(self, space_id: str, departure_time: datetime):
        if not self.is_occupied(space_id):
            raise ValueError('There is no vehicle in the space provided')
        
        parking_activity = find(self.parking_activity, lambda pa: pa.active and pa.space_id == space_id)

        parking_activity.departure_time = departure_time

    @property
    def parking(self):
        return self.__parking
    
    
    @property
    def parking_activity(self):
        return self.__parking_activity
    
    @property
    def available_prices(self):
        return self.parking.available_prices