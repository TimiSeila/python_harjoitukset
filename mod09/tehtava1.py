class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

car = Car("ABC-123", 142)

print(f"Auton rekisterinumero: {car.registration_number}")
print(f"Auton maksiminopeus: {car.max_speed}km/h")
print(f"Auton tämänhetkinen nopeus: {car.current_speed}km/h")
print(f"Kokonaismatka ajettu: {car.travelled_distance}km")
