number = input("Syötä luku: ")

try:
    int(number)
except:
    print("Virheellinen luku")
    exit()

for index in range(1, int(number) + 1):
    if index == int(number) and int(number) != 1:
        print("Luku on alkuluku")
        break

    if int(number) % index == 0 or int(number) != 1:
        print("Luku ei ole alkuluku")
        break
