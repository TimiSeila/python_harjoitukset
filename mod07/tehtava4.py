test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sum_of_list(integer_list):
    sum = 0

    for integer in integer_list:
        sum += integer

    return sum

print(f"Lista {test_list}")
print(f"Summa: {sum_of_list(test_list)}")
