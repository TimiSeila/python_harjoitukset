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
    print("2. Asetukset")
    print("3. Lopeta")
    komento = input("Valitse toiminto (1-3): ")

    if komento == "1":
        print("Peli")
    if komento == "2":
        print("Asetukset")
    if komento == "3":
        break
