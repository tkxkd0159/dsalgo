def power_recur(x, y: int):
    if y == 0:
        return 1

    recur = power_recur(x, y // 2)
    if (y % 2 == 0):
        return recur * recur
    else:
        return recur * recur * x

def power(x, y):

    base = x
    sum_ = 1

    while y > 0:
        if (y & 1) == 1: # filter odd number
            sum_ *= base
        base = base * base
        y = y >> 1

    return sum_


print(power_recur(3, 5) == power(3, 5))
print(power_recur(5, 6) == power(5, 6))
print(power_recur(7, 9) == power(7, 9))

print(4 & 1)