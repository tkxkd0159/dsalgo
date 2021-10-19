# 계단 수를 n이라 할 때 한 계단 또는 두 계단씩 올라가서 끝까지 올라가는 경우의 수

from math import factorial

def myfac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * myfac(n-1)

def staircase(n):
    if n < 1:
        return 1

    if n % 2 == 0:
        cnt2 = int(n / 2)
    else:
        cnt2 = int((n-1) / 2)

    total = 0
    for i in range(cnt2+1):
        cnt1 = n - 2*i
        total += (factorial(i+cnt1)/factorial(i)/factorial(cnt1))

    return int(total)

def staircase_ans(n):  # staircase(n) = staircase(n-1) + staircase(n-2), n번 계단으로 가기 위해서는 n−1번 계단 또는 n−2번 계단에서 올라가야 한다
    a, b = 1, 1        # 0, 1th
    for _ in range(n):
        a, b = b, a + b
    return a


# 테스트
print(staircase(0))
print(staircase(2))
print(staircase(4))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))