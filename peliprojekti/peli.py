inventory = []

def gameloop():
    print("Peli")

def add_to_inventory():
    print("Lisää tavara reppuun:")
    print("1. Miekka")
    print("2. Kilpi")

    komento = input("Valitse toiminto (1-2): ")

    if komento == "1":
        inventory.append("Miekka")
    if komento == "2":
        inventory.append("Kilpi")

def show_inventory():
    print("Repussasi on:")
    for item in inventory:
        print(item)

def quit():
    print("Peli loppui")
name = input("Anna nimesi: ")
age = input("Anna ikäsi: ")

try:
    int(age)
except:
    print("Virheellinen ikä")
    exit()

if int(age) < 12:
    print("Olet alaikäinen")
    exit()

print("Hei,", name)

komento = ""
while True:
    print("1. Pelaa")
    print("2. Reppu")
    print("3. Näytä repun sisältö")
    print("4. Lopeta")
    komento = input("Valitse toiminto (1-4): ")

    if komento == "1":
        gameloop()
    if komento == "2":
        add_to_inventory()
    if komento == "3":
        show_inventory()
    if komento == "4":
        quit()
        break
