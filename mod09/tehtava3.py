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

car = Car("ABC-123", 142)

car.accelerate(60)
car.drive(1.5)

car.accelerate(30)
car.accelerate(70)

print(f"Auton rekisterinumero: {car.registration_number}")
print(f"Auton maksiminopeus: {car.max_speed}km/h")
print(f"Auton tämänhetkinen nopeus: {car.current_speed}km/h")
print(f"Kokonaismatka ajettu: {car.travelled_distance}km")

print("Hätäjarrutus...")
car.accelerate(-200)

print(f"Auton tämänhetkinen nopeus: {car.current_speed}")
