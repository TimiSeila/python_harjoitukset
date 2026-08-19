FISH_LENGTH_LIMIT_CM = 37

fish_length = input("Anna kuhan pituus senttimetreinä: ")

if float(fish_length) < FISH_LENGTH_LIMIT_CM:
    print("Palauta kala veteen, kala on", FISH_LENGTH_LIMIT_CM - float(fish_length), "cm liian pieni")
