from DriverMan import DriverMan
from Vehicle import Vehicle

class DriverManager:
    driver_man_list: list[DriverMan] = []

    def add(self, driver: DriverMan):
        if driver.age < 18:
            raise ValueError("driver age must be at least 18")


class VehicleManager:
    vehicle_list: list[Vehicle] = []

    def add(self, driver: Vehicle):
        if driver.age > 10:
            raise ValueError("vehicle must less than 10 years old")
