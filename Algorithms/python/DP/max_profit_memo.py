def max_profit_memo(price_list, count, cache):
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    if count in cache:
        return cache[count]

    # profit은 count개를 팔아서 가능한 최대 수익을 저장하는 변수
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 profit에 저장
    for i in range(1, count // 2 + 1):
        profit = max(profit, max_profit_memo(price_list, i, cache)
                 + max_profit_memo(price_list, count - i, cache))

    # 계산된 최대 수익을 cache에 저장
    cache[count] = profit

    return profit

def max_profit_memo2(price_list, count, cache):
    if count == 0:
        cache[0] = price_list[0]
        return cache[0]
    elif count == 1:
        cache[1] = price_list[1]
        return cache[1]
    elif count in cache:
        return cache[count]

    max_p = 0
    for i in range(1, count+1):
        if count < len(price_list) and i == count:
            temp = price_list[i]
        else:
            temp = max_profit_memo2(price_list, i, cache) + max_profit_memo2(price_list, count-i, cache)
        if temp > max_p:
            max_p = temp
            cache[count] = max_p

    return cache[count]

def max_profit_ans(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)

def max_profit2(price_list, count):
    max_profit_cache = {}

    return max_profit_memo2(price_list, count, max_profit_cache)


if __name__ == "__main__":
    # 개수별 가격, 2번 케이스의 경우 개수별 가격이 정해진 것 보다 판매할 개수가 더 많음
    print(max_profit_ans([0, 100, 400, 800, 900, 1000], 5))
    print(max_profit_ans([0, 100, 400, 800, 900, 1000], 10))
    print(max_profit_ans([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
    print(max_profit2([0, 100, 400, 800, 900, 1000], 5))
    print(max_profit2([0, 100, 400, 800, 900, 1000], 10))
    print(max_profit2([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))