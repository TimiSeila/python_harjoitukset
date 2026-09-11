numbers = []

while True:
    number = input("Syötä numero: ")

    if number == "":
        break

    try:
        int(number)
    except:
        print("Virheellinen numero")
        exit()

    numbers.append(int(number))

numbers.sort(reverse=True)

for index, number in enumerate(numbers[0:5]):
    print(f"{index + 1}. {number}")
