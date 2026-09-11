import random

def roll_die(die_face_count):
    return random.randint(1, die_face_count) 

die_face_count_input = input("Syötä nopan sivujen lukumäärä: ")

try:
    int(die_face_count_input)
except:
    print("Virheellinen lukumäärä")
    exit()

while True:
    roll_result = roll_die(int(die_face_count_input))

    print("Heitetään noppaa...")
    print(f"Tulos: {roll_result}")

    if(roll_result != int(die_face_count_input)):
        print(f"Tulos ei ollut {die_face_count_input}. Yritetään uudelleen...")
    else:
        break
