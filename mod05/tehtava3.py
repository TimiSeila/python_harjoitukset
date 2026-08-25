current_min = 0
current_max = 0

while True:

    input_num = input("Anna luku: ")

    if input_num == "":
        break

    try:
        float(input_num)
    except:
        print("Virheellinen luku")
        print("Pienin syötetty luku:", current_min)
        print("Suurin syötetty luku:", current_max)
        exit()

    if float(input_num) < current_min:
        current_min = float(input_num)
    if float(input_num) > current_max:
        current_max = float(input_num)

print("Ohjelma lopetettu")
print("Pienin syötetty luku:", current_min)
print("Suurin syötetty luku:", current_max)
