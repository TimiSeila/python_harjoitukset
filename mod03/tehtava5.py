import math

leivs = input("Anna leiviskät: ")
nails = input("Anna naulat: ")
bullets = input("Anna luodit: ")
BULLET_WEIGHT_G = 13.3

leivs_in_grams = float(leivs) * 20 * 32 * BULLET_WEIGHT_G
nails_in_grams = float(nails) * 32 * BULLET_WEIGHT_G
bullets_in_grams = float(bullets) * BULLET_WEIGHT_G

grams = leivs_in_grams + nails_in_grams + bullets_in_grams
kilograms = math.floor(grams / 1000)

print("Massa nykymittojen mukaan on:", str(kilograms) + "kg", str(round(grams - kilograms * 1000, 2)) + "g")
