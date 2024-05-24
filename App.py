from ParkingLot import ParkingLot
from DriverMan import DriverMan
from Vehicle import Vehicle
from Managers import DriverManager, VehicleManager

from datetime import datetime

class App:
    opened = True
    parking_lot: ParkingLot
    vehicles_manager = VehicleManager()
    driver_man_manager = DriverManager()

    def collect_parking_lot_data(self):
        possible_dimentions = ((6, 6), (8, 8), (10, 10))

        print(' - Please, choose the dimention of the parking')
        
        for index, dimention in enumerate(possible_dimentions):
            # show enumarated list of the possible options
            # with index incremented by one. Ej: 1. 6x6
            print(f"{index + 1}. {dimention[0]}x{dimention[1]}")
        
        taken_option = int(input('option number: ')) - 1

        if not 0 <= taken_option <= 2:
            raise ValueError("Invalid option")

        dimention_selected = possible_dimentions[taken_option]

        self.parking_lot = ParkingLot(dimention_selected[0])

    
    def collect_driver_man_data(self):
        driver_id = input('driver id: ')
        driver_name = input('driver name: ')

        driver_date_str = input('driver date of birth (AAAA/MM/DD): ')
        driver_date = datetime.strptime(driver_date_str, "%Y/%m/%d").date()

        driver_sex = input('sex (M/F): ')

        available_prices = self.parking_lot.available_prices
        for num, price in enumerate(available_prices):
            print(f"{num + 1}. {price}")
        user_input = input('choose your goal price: ')
        driver_goal_layer = int(user_input) - 1

        new_driver = DriverMan(driver_id, driver_name, driver_date, driver_sex, driver_goal_layer)
        self.driver_man_manager.add(new_driver)
        return new_driver
    
    
    def collect_vehicle_data(self):
        v_plate = input('vehicle plate: ')
        v_mark = input('vehicle mark: ')
        v_name = input('vehicle name: ')

        new_vehicle = Vehicle(v_plate, v_mark, v_name)
        self.vehicles_manager.add(new_vehicle)
        return new_vehicle


    def assign_space(self):
        v_plate = input('vehicle plate: ')


    def exit(self):
        self.opened = False


    def run(self):
        self.collect_parking_lot_data()


        options = [
            { "msg": "assign space to a new vehicle", "func": self.assign_space },
            { "msg": "exit", "func": self.exit }
        ]

        while self.opened:

            self.collect_driver_man_data()


if __name__ == '__main__':
    app = App()
    app.run()