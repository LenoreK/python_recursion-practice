numbers = [1, 2, 3, 4]
def multi_list(list):
    result = 1
    for x in list:
        result = result * x
    return result

print(multi_list(numbers))