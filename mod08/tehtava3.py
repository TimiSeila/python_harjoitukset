airports = {}

def menu():
    print("Valitse toiminto:")
    print("    1. Syötä uusi lentoasema")
    print("    2. Hae lentoasemaa")
    print("    3. Lopeta")
    selection = input("(1-3): ")

    match selection:
        case "1":
            icao = input("Syötä ICAO-koodi: ")
            name = input("Syötä lentoaseman nimi: ")
            status = add_airport(icao, name)

            match status:
                case "created":
                    print(f"Lentoasema {name} lisätty ICAO-koodilla {icao.upper()}")
                case "updated":
                    print(f"Lentoaseman {icao.upper()} nimi päivitetty: {name}")
                case _:
                    print("Tapahtui virhe, yritä uudelleen")
        case "2":
            icao = input("Syötä ICAO-koodi: ")
            airport = fetch_airport(icao)

            if airport is None:
                print(f"Lentoasemaa ICAO-koodilla {icao.upper()} ei löytynyt")
            else:
                print(f"Lentoaseman {icao.upper()} nimi on {airport}")
        case "3":
            exit()
        case _:
            print("Virheellinen syöte")

def fetch_airport(icao):
    icao_upper = icao.upper()

    found_airport = airports.get(icao_upper)

    return found_airport

def add_airport(icao, name):
    icao_upper = icao.upper()

    found_airport = fetch_airport(icao_upper)

    if found_airport is None:
        airports[icao_upper] = name
        return "created"
    elif found_airport:
        airports[icao_upper] = name
        return "updated"

while True:
    menu()
