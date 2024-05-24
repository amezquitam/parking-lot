from DriverMan import DriverMan
from Vehicle import Vehicle
from Managers import DriverManager, VehicleManager, ParkingManager

from datetime import datetime

class App:
    opened = True
    parking_manager: ParkingManager
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

        self.parking_manager = ParkingManager(dimention_selected[0])

    
    def collect_driver_man_data(self, driver_id):
        if driver_id is None:
            driver_id = input('driver id: ')
        driver_name = input('driver name: ')

        driver_date_str = input('driver date of birth (AAAA/MM/DD): ')
        driver_date = datetime.strptime(driver_date_str, "%Y/%m/%d").date()

        driver_sex = input('sex (M/F): ')

        available_prices = self.parking_manager.available_prices
        for num, price in enumerate(available_prices):
            print(f"{num + 1}. {price}")
        user_input = input('choose your goal price: ')
        driver_goal_layer = int(user_input) - 1

        new_driver = DriverMan(driver_id, driver_name, driver_date, driver_sex, driver_goal_layer)
        self.driver_man_manager.add(new_driver)
        return new_driver
    
    
    def collect_vehicle_data(self, v_plate: str | None, v_owner_id: str):
        if v_plate is None:
            v_plate = input('vehicle plate: ')
        v_mark = input('vehicle mark: ')
        v_year = int(input('vehicle year: '))

        new_vehicle = Vehicle(v_plate, v_mark, v_year, v_owner_id)
        self.vehicles_manager.add(new_vehicle)
        return new_vehicle


    def assign_space(self):
        driver_id = input('driver id: ')
        if not self.driver_man_manager.contains(driver_id):
            driver = self.collect_driver_man_data(driver_id)
        else: driver = self.driver_man_manager.find(v_plate)

        v_plate = input('vehicle plate: ')
        if not self.vehicles_manager.contains(v_plate):
            vehicle = self.collect_vehicle_data(v_plate, driver_id)
        else: vehicle = self.vehicles_manager.find(v_plate)
        
        if vehicle.owner_id != driver_id:
            raise ValueError('this vehicle alreary registered with other owner')
        
        entry_time_str = input('entry time (aaaa/mm/dd hh:mm): ')
        entry_time = datetime.strptime(entry_time_str, '%Y/%m/%d %H:%M')
        
        self.parking_manager.assign_space_to_vehicle(v_plate, driver.preferred_layer, entry_time)

    
    def take_out_a_vehicle(self):
        space_id = input('space id: ')
        departure_time_str = input('departure time (aaaa/mm/dd hh:mm): ')
        departure_time = datetime.strptime(departure_time_str, '%Y/%m/%d %H:%M')

        self.parking_manager.take_out_vehicle(space_id, departure_time)


    def show_free_spaces(self):
        free_spaces = self.parking_manager.free_spaces_matrix()
        letters = 'ABCDEFGHIJLM'

        print('    ', end='')
        for letter in letters[:self.parking_manager.parking.size]:
            print(f' {letter} ', end=' ')
        print()

        for num, column in enumerate(free_spaces):
            print(' %.2d ' % (num + 1), end='')
            for is_space_occupied in column:
                print('[O]' if is_space_occupied else '[ ]', end=' ')
            print()


    def exit(self):
        self.opened = False


    def run(self):
        self.collect_parking_lot_data()

        options = [
            { "msg": "assign space to a new vehicle", "func": self.assign_space },
            { "msg": "take out a vehicle", "func": self.take_out_a_vehicle },
            { "msg": "show free spaces", "func": self.show_free_spaces },
            { "msg": "exit", "func": self.exit }
        ]

        while self.opened:
            for num, option in enumerate(options):
                print(f'{num + 1}. {option["msg"]}')
            
            user_option = int(input('your option: ')) - 1

            options[user_option]['func']()


if __name__ == '__main__':
    app = App()
    app.run()