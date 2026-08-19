gender = input("Anna sukupuolesi: ")
hemoglobin = input("Anna hemoglobiiniarvosi(g/L): ")

try:
    float(hemoglobin)
except:
    print("Virheellinen hemoglobiiniarvo")
    exit()

if gender.upper() == "NAINEN":
    if float(hemoglobin) < 117:
        print("Hemoglobiinisi on alhainen")
    elif float(hemoglobin) > 175:
        print("Hemoglobiinisi on korkea")
    elif 117 <= float(hemoglobin) <= 175:
        print("Hemoglobiinisi on normaali")

elif gender.upper() == "MIES":
    if float(hemoglobin) < 134:
        print("Hemoglobiinisi on alhainen")
    elif float(hemoglobin) > 195:
        print("Hemoglobiinisi on korkea")
    elif 134 <= float(hemoglobin) <= 195:
        print("Hemoglobiinisi on normaali")

else:
    print("Virheellinen sukupuoli:", gender)
