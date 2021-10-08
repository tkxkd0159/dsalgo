#### Brute Force ####

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


#### Divide And Conquer ####


def max_crossing_sum(profits, start, end):
    """
    중앙을 가로지르는 가장 큰 합 구하기
    """
    mid = (start + end) // 2
    '''
    왼쪽에서의 가장 큰 수익 계산
    인덱스 mid부터 인덱스 0까지 범위를 넓혀가며 최대 수익을 찾는다
    '''
    left_sum = 0
    left_max = profits[mid]

    for i in range(mid, start - 1, -1):
        left_sum += profits[i]
        left_max = max(left_max, left_sum)

    '''
    오른쪽에서의 가장 큰 수익 계산
    인덱스 mid+1부터 인덱스 end까지 범위를 넓혀가며 최대 수익을 찾는다
    '''
    right_sum = 0
    right_max = profits[mid + 1]

    for i in range(mid + 1, end + 1):
        right_sum += profits[i]
        right_max = max(right_max, right_sum)

    return left_max + right_max


def sublist_max_dnq(profits, start, end):
    if start == end:
        return profits[start]

    mid = (start + end) // 2

    max_left = sublist_max_dnq(profits, start, mid)
    max_right = sublist_max_dnq(profits, mid + 1, end)
    max_cross = max_crossing_sum(profits, start, end)

    return max(max_left, max_right, max_cross)


# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max_dnq(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max_dnq(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max_dnq(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max_dnq(list4, 0, len(list4) - 1))