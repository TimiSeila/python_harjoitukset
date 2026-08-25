INCH_IN_CM = 2.54

while True:
    inches = input("Anna tuumat: ")

    try:
        float(inches)
    except:
        print("Virheellinen tuuma")
        break

    if(float(inches) < 0):
        print("Virheellinen tuuma")
        break

    print("Tuuma(a) muunnettuna senttimetreihin on:", float(inches) * INCH_IN_CM)
