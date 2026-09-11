cities = []

for index in range(1, 6):
    city = input(f"Anna kaupunki numero {index}: ")
    cities.append(city)

for index, city in enumerate(cities):
    print(f"{index + 1}. {city}")
