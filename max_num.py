def max_num(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif(b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return(largest)

print(max_num(1, 2, 3))

#max function! - That is so much easier.