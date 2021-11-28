def rev_int(n):
    reversed = str(n)
    reversed[::-1]

    return int(reversed) * negative_condition(n)


def negative_condition(n):
    if(n < 0):
        n * -1
    else:
        n * 1


result = rev_int(-45)
print(result)
