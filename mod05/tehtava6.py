import random
import math
import time

attempt = 1
points_inside_circle = 0

max_points = input("Syötä pisteiden määrä: ")

try:
    int(max_points)
except:
    print("Virheellinen määrä pisteitä")
    exit()

while attempt <= int(max_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x * x + y * y <= 1:
        points_inside_circle += 1

    attempt += 1

circle_area = (points_inside_circle / int(max_points)) * 4
print("PI:", circle_area)
