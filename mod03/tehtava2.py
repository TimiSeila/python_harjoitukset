import math

r = input("Anna ympyrän säde: ")

try:
    float(r)
except:
    print("Virheellinen säde")
    exit()

area = math.pi * (float(r) * float(r))

print("Pinta-ala:", area)
