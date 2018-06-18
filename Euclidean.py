number_1 = 727
number_2 = 119
def GCD(number_1,number_2):
    while number_1 != number_2:
        if number_1 > number_2:
            big = number_1
            small = number_2
            diff = big - small
            number_1 = diff
        else:
            number_1,number_2 = number_2,number_1
    return number_1
result = GCD(number_1,number_2)
print(result)