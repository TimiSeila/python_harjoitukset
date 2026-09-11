def gallons_to_liters(gallons):
    return round(gallons * 4.54609, 2)

while True:
    gallons_input = input("Syötä gallonat: ")

    try:
        float(gallons_input)
    except:
        print("Virheellinen gallona arvo")
        exit()

    if float(gallons_input) < 0:
        break

    print(f"{gallons_input} gallonaa on noin {gallons_to_liters(float(gallons_input))} litraa")
