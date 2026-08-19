cabin_class = input("Anna hyttisi luokka (LUX, A, B, C): ")

if cabin_class.upper() == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella")
elif cabin_class.upper() == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif cabin_class.upper() == "B":
    print("B on ikkunaton hytti autokannen yläpuolella")
elif cabin_class.upper() == "C":
    print("C on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka:", cabin_class)
