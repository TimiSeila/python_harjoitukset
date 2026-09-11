import random

count = input("Anna arpakuutioiden lukumäärä: ")

try:
    int(count)
except:
    print("Virheellinen lukumäärä")
    exit()

sum = 0
for digit in range(1, int(count) + 1):
    die_result = random.randint(1, 6)
    print(f"{int(digit)}. {die_result}")
    sum += die_result

print(f"Summa: {sum}")
