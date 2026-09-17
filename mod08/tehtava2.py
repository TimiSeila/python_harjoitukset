names = set()

while True:
    name = input("Syötä nimi: ")

    if name == "":
        break

    starting_length = len(names)
    names.add(name)

    if len(names) == starting_length:
        print("Nimi on syötetty aikaisemmin")
    else:
        print("Nimi lisätty listaan")

print(names)
