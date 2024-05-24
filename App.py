from ParkingLot import ParkingLot

class App:
    parking_lot: ParkingLot

    def collect_data_about_parking_lot(self):
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


    def run(self):
        self.collect_data_about_parking_lot()
        pass


if __name__ == '__main__':
    app = App()
    app.run()