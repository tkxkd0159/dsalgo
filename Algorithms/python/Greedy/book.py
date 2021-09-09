# This is coding test

def change(n):
    count = 0
    coin_types = [500, 100, 50, 10]
    for c in coin_types:
        count += n // c
        n %= c

    return count

def max_plus(case):
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))

    data.sort(reverse=True)
    first = data[0]
    second = data[1]
    res = 0

    if case == 1:
        for i in range(1, m+1):
            if i % (k+1) == 0:
                res += second
                print(i)
            else:
                res += first

    elif case == 2:
        count = int(m / (k + 1)) * k
        count += m % (k + 1)
        res += count * first
        res += (m - count) * second

    return res

def num_cardgame():
    h, w = map(int, input().split())
    res = []
    for _ in range(h):
        res.append(min(list(map(int, input().split()))))

    return max(res)

print(num_cardgame())