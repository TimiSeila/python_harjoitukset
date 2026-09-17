class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = 0

    def floor_up(self):
        self.current_floor += 1
        print(f"Tällä hetkellä kerroksessa {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"Tällä hetkellä kerroksessa {self.current_floor}")

    def go_to_floor(self, destination_floor):
        floors_in_between = destination_floor - self.current_floor

        if floors_in_between == 0:
            return

        if floors_in_between > 0:
            for i in range(floors_in_between):
                self.floor_up()
        else:
            for i in range(abs(floors_in_between)):
                self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(number_of_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, target_elevator_index, destination_floor):
        print(f"Hissi numero {target_elevator_index} liikkuu")
        self.elevators[target_elevator_index + 1].go_to_floor(destination_floor)
        
building = Building(0, 15, 4)
building.run_elevator(1, 4)
