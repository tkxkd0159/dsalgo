def fib_memo(n, cache):
    if n < 3:
        return 1

    if n in cache:
        return cache[n]

    # 함수 콜스택 쌓이고 cache에 차례로 값이 memoization 됨
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

    return cache[n]


def fib(n):
    fib_cache = {}

    return fib_memo(n, fib_cache)


N = 1000
d = [0 for _ in range(N)]


def fib_arr_topdown(n):
    if n < 3:
        return 1
    if d[n] != 0:
        return d[n]

    d[n] = fib_arr_topdown(n - 1) + fib_arr_topdown((n - 2))

    return d[n]


d[1], d[2] = 1, 1


def fib_arr_botup(n):
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[n]


if __name__ == "__main__":
    print(fib(10))
    print(fib(50))
    print(fib(100))
    print(fib_arr_topdown(100))
    print(fib_arr_botup(100))
