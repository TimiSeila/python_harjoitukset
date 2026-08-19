print("Anna 3 lukua")
num1 = input("Luku 1: ")
num2 = input("Luku 2: ")
num3 = input("Luku 3: ")

try:
    float(num1)
    float(num2)
    float(num3)
except:
    print("Virheellinen luku syötetty")
    exit()

sum = float(num1) + float(num2) + float(num3)
product = float(num1) * float(num2) * float(num3)
average = sum / 3

print("Summa:", sum)
print("Tulo:", product)
print("Keskiarvo:", average)
