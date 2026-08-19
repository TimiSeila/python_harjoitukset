import random

print("Koodit:")

three_digit_code = str(random.randint(0, 9)) + ", " + str(random.randint(0, 9)) + ", " + str(random.randint(0, 9))
four_digit_code = str(random.randint(1, 6)) + ", " + str(random.randint(1, 6)) + ", " + str(random.randint(1, 6)) + ", " + str(random.randint(1, 6))

print("Kolminumeroinen:", three_digit_code)
print("Nelinumeroinen:", four_digit_code)
