USERNAME = "teng0ni"
PASSWORD = "1234"

attempt = 1

while attempt <= 5:
    input_username = input("Käyttäjätunnus: ")
    input_password = input("Salasana: ")

    if input_username == USERNAME and input_password == PASSWORD:
        print("Tervetuloa!")
        break
    else:
        print("Yritä uudestaan")
    attempt += 1
else:
    print("Pääsy evätty!")
