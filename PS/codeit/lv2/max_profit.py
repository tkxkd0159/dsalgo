def max_profit(stock_list):
    diff_ls = []
    for i in range(1, len(stock_list)):
        diff_ls.append(stock_list[i] - stock_list[i-1])

    max_diff_chk = diff_ls[0]
    max_diff_so_far = diff_ls[0]
    for i in range(1, len(diff_ls)):
        max_diff_chk = max(max_diff_chk+diff_ls[i], diff_ls[i])
        max_diff_so_far = max(max_diff_chk, max_diff_so_far)

    return max_diff_so_far


def max_profit2(stock_list): # 투포인터 같은 풀이 (?)
    max_profit_so_far = stock_list[1] - stock_list[0]
    min_so_far = min(stock_list[0], stock_list[1])

    for i in range(2, len(stock_list)):
        max_profit_so_far = max(max_profit_so_far, stock_list[i] - min_so_far)

        # 현재 주식 가격이 최솟값인지 확인한다
        min_so_far = min(min_so_far, stock_list[i])

    return max_profit_so_far


# 테스트, 한 날 사서 이후 특정 날에 팔 때 최대 수익 리턴
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))