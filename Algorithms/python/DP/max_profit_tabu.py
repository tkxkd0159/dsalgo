def max_profit(price_list, count):
    profits = price_list
    for _ in range(count-len(price_list)+1):
        profits.append(0)

    if count < 2:
        return profits[count]

    for i in range(2, count + 1):
        for j in range(1, i // 2 + 1):
            profits[i] = max(profits[i], profits[j] + profits[i-j])

    return profits[count]

def max_profit2(price_list, count):
    profit_table = [0]

    for i in range(1, count + 1):
        profit = price_list[i] if i < len(price_list) else 0

        for j in range(1, i // 2 + 1):
            profit = max(profit, profit_table[j] + profit_table[i - j])

        profit_table.append(profit)

    return profit_table[count]


if __name__ == "__main__":
    print(max_profit([0, 200, 600, 900, 1200, 2000], 2))
    print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
    print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
    print(max_profit2([0, 200, 600, 900, 1200, 2000], 2))
    print(max_profit2([0, 300, 600, 700, 1100, 1400], 8))
    print(max_profit2([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
