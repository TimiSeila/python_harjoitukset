number_of_month = input("Syötä kuukauden numero: ")
seasons = ("Kevät", "Kesä", "Syksy", "Talvi")

try:
    int(number_of_month)
except:
    print("Virheellinen syöte")
    exit()

if int(number_of_month) >=1 and int(number_of_month) <= 3:
    print(seasons[0])
elif int(number_of_month) >= 4 and int(number_of_month) <=6:
    print(seasons[1])
elif int(number_of_month) >= 7 and int(number_of_month) <= 9:
    print(seasons[2])
elif int(number_of_month) >= 10 and int(number_of_month) <= 12:
    print(seasons[3])
else:
    print(f"Ei ole kuukautta numero {number_of_month}")
