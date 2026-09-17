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

elevator = Elevator(0, 15)
elevator.go_to_floor(10)
elevator.go_to_floor(0)
