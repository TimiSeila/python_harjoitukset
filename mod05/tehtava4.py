import random

target_num = random.randint(1, 10)

while True:
    input_num = input("Arvaa luku 1 - 10: ")

    try:
        float(input_num)
    except:
        print("Virheellinen luku")
        exit()

    if float(input_num) == target_num:
        print("Voitit!")
        break
    if float(input_num) < target_num:
        print("Liian pieni arvaus")
        continue
    if float(input_num) > target_num:
        print("Liian suuri arvaus")
        continue
