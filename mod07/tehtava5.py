test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def remove_odd_integers(integer_list):
    integer_list_copy = integer_list.copy()

    for integer in integer_list_copy:
        if integer % 2 != 0:
            integer_list_copy.remove(integer)

    return integer_list_copy 

print(f"Lista {test_list}")
print(f"Lista ilman parittomia lukuja: {remove_odd_integers(test_list)}")
