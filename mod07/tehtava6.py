import math

def calculate_square_m_cost(diameter, cost):
    pizza_area = round((diameter / 2) ** 2 * math.pi / 10000, 4)
    cost_per_square_m = round(cost / pizza_area, 2)

    return cost_per_square_m 

pizza1_diameter = input("Anna 1. pizzan halkaisija (cm): ")
pizza2_diameter = input("Anna 2. pizzan halkaisija (cm): ")

pizza1_cost = input("Anna 1. pizzan hinta (€): ")
pizza2_cost = input("Anna 2. pizzan hinta (€): ")

try:
    float(pizza1_diameter)
    float(pizza2_diameter)
    float(pizza1_cost)
    float(pizza2_cost)
except:
    print("Virheellinen syöte")
    exit()

pizza1_cost_per_square_meter = calculate_square_m_cost(float(pizza1_diameter), float(pizza1_cost))
pizza2_cost_per_square_meter = calculate_square_m_cost(float(pizza2_diameter), float(pizza2_cost))

if pizza1_cost_per_square_meter < pizza2_cost_per_square_meter:
    print("1. Pizza on halvempi kuin 2. pizza")
else:
    print("2. Pizza on halvempi kuin 1. pizza")
