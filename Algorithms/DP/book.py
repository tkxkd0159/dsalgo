def make1(n):
    tabu = [0 for _ in range(30000)]
    for i in range(2, n + 1):
        tabu[i] = tabu[i - 1] + 1
        if i % 2 == 0:
            tabu[i] = min(tabu[i], tabu[i // 2] + 1)
        if i % 3 == 0:
            tabu[i] = min(tabu[i], tabu[i // 3] + 1)
        if i % 5 == 0:
            tabu[i] = min(tabu[i], tabu[i // 5] + 1)

    return tabu[n]


def ant_warrior(n, food_storages):
    tabu_food = [0 for _ in range(100)]
    tabu_food[0] = food_storages[0]
    tabu_food[1] = max(food_storages[1], food_storages[0])
    for i in range(2, n):
        tabu_food[i] = max(tabu_food[i - 1], tabu_food[i - 2] + food_storages[i])
    return tabu_food[n - 1]


def floorWork(n):
    tabu = [0 for _ in range(n)]
    tabu[0] = 1
    tabu[1] = 3
    for i in range(2, n):
        tabu[i] = (tabu[i-2] * 2 + tabu[i-1]) % 796796

    return tabu[n-1]


def pickMoney(target_money, currency_ls):
    tabu = [10001 for _ in range(target_money+1)]
    tabu[0] = 0

    for i in range(len(currency_ls)):
        for j in range(currency_ls[i], target_money+1):
            tabu[j] = min(tabu[j], tabu[j-currency_ls[i]] + 1)

    if tabu[target_money] != 10001:
        return tabu[target_money]
    else:
        return -1




if __name__ == '__main__':
    print(make1(26))
    print(ant_warrior(4, [1, 3, 1, 5]))
    print(floorWork(3))
    print(pickMoney(4, [3, 5, 7]))
    print(pickMoney(15, [2, 3]))
