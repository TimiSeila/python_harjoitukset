import random 

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

        if self.current_speed < 0:
            self.current_speed = 0

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours_driven):
        self.travelled_distance += round(self.current_speed * hours_driven, 2)

class Race:
    def __init__(self, name, length, cars):
        self.name = name
        self.length = length
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self, current_hour):
        print("----------------\n")
        print(f"Tulokset tunnilta {current_hour}")
        for car in self.cars:
            print(f"Auton rekisterinumero: {car.registration_number}")
            print(f"Auton maksiminopeus: {car.max_speed}km/h")
            print(f"Auton tämänhetkinen nopeus: {car.current_speed}km/h")
            print(f"Kokonaismatka ajettu: {car.travelled_distance}km")
            print("--------")
        print("----------------")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.length:
                return True

        return False

car_list = []
for i in range(10):
    car_list.append(Car("ABC-" + str(i + 1), random.randint(100, 200)))

gdd = Race("Grand Demolition Derby", 8000, car_list)

current_hour = 1
while True:
    gdd.hour_passes()
    if gdd.race_finished():
        gdd.print_status(current_hour)
        break

    if current_hour % 10 == 0:
        gdd.print_status(current_hour)

    current_hour += 1

