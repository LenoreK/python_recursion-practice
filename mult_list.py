numbers = [1, 2, 3, 4]
def multi_list(list):
    result = 1
    for x in list:
        result = result * x
    return result

print(multi_list(numbers))

#def mult_list(list):
#    if len(list) == 0:
#        return 0
#    prod = list[0]
#
#    if len(list) > 1:
#        for i in list[1:]:
#            prod = prod * 1