year = input("Anna vuosi: ")
is_leap_year = False

try:
    float(year)
except:
    print("Virheellinen vuosi")
    exit()

if float(year) % 4 == 0 and float(year) % 100 != 0 or float(year) % 400 == 0:
    is_leap_year = True

if(is_leap_year):
    print("Vuosi", year, "on karkausvuosi")
else:
    print("Vuosi", year, "ei ole karkausvuosi")
