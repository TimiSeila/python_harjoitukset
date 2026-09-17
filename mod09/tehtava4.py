import random 

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 2000

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

        if self.current_speed < 0:
            self.current_speed = 0

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours_driven):
        self.travelled_distance += round(self.current_speed * hours_driven, 2)

car_list = []
for i in range(10):
    car_list.append(Car("ABC-" + str(i + 1), random.randint(100, 200)))


current_hour = 1
race_has_winner = False
while not race_has_winner:
    print(f"Tulokset tunnilta {current_hour}")
    print("----------------\n")
    for car in car_list:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_has_winner = True

        print(f"Auton rekisterinumero: {car.registration_number}")
        print(f"Auton maksiminopeus: {car.max_speed}km/h")
        print(f"Auton tämänhetkinen nopeus: {car.current_speed}km/h")
        print(f"Kokonaismatka ajettu: {car.travelled_distance}km")
        print("--------")

    print("----------------")
    current_hour += 1



