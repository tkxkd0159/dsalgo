def sublist_max(profits):
    max_profit = 0
    tmp = 0
    for i in range(len(profits)):
        tmp = profits[i]
        if profits[i] > max_profit:
            max_profit = i
        for j in range(1, len(profits)):
            if j <= i:
                continue
            tmp += profits[j]
            if tmp > max_profit:
                max_profit = tmp
    return max_profit

def sublist_max_ans(profits):
    max_profit = profits[0]

    for i in range(len(profits)):
        total = 0

        for j in range(i, len(profits)):
            total += profits[j]

            max_profit = max(max_profit, total)


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))