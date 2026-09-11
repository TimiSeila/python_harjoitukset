import random

def roll_die():
    return random.randint(1, 6) 

while True:
    roll_result = roll_die()

    print("Rolling the die...")
    print(f"Result: {roll_result}")

    if(roll_result != 6):
        print("Didn't get 6. Trying again...")
    else:
        break
