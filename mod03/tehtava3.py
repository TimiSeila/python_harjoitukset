import math

base = input("Anna suorakulmion kanta: ")
height = input("Anna suorakulmion korkeus: ")

try:
    float(base)
    float(height)
except:
    print("Virheellinen kanta tai korkeus")
    exit()

perimeter = float(base) * 2 + float(height) * 2 
area = float(base) * float(height)

print("Piiri:", perimeter)
print("Pinta-ala:", area)
