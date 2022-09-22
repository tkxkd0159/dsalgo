import sys


def solve2525():
    h, m = map(int, input().split())
    work, = map(int, input().split())

    tot = 60*h + m + work
    cycle = 24 * 60
    if tot >= cycle:
        tot %= cycle
    h = tot // 60
    m = (tot - h*60)

    print(f'{h} {m}')


def solve2480():
    f, s, t = map(int, input().strip().split())

    res: int

    dice = [0] * 7
    dice[f] += 1
    dice[s] += 1
    dice[t] += 1
    same = 1
    res = (same, None)
    for i in range(1, len(dice)):
        if dice[i] > res[0]:
            res = (dice[i], i)

    if res[0] == 1:
        out = max(f, s, t) * 100
    elif res[0] == 2:
        out = res[1] * 100 + 1000
    elif res[0] == 3:
        out = res[1] * 1000 + 10000

    print(out)


def solve2739():
    n, = map(int, input().strip().split())
    for i in range(1, 10):
        print(f'{n} * {i} = {n*i}')


def solve10950():
    n, = map(int, input().strip().split())
    for i in range(n):
        f, s = map(int, input().strip().split())
        print(f+s)


def solve1110():
    N = int(input().strip())
    n = -1
    rep = 0
    while n != N:
        if n == -1:
            n = N
        n = (n//10 + n % 10) % 10 + (n % 10)*10
        rep += 1
    print(rep)


def solve3052():
    b = [int(input()) % 42 for i in range(10)]
    print(len(set(b)))


def solve1546():
    n, *scores = map(int, sys.stdin.buffer.read().split())
    M = max(scores)
    new_scores = [i/M*100 for i in scores]
    print(sum(new_scores)/n)


def solve2920():
    print({"12345678": "ascending", "87654321": "descending"}.get(
        input()[::2], "mixed"))


def solve10809():
    s = input().strip()
    a = "abcdefghijklmnopqrstuvwxyz"
    for i in a:
        print(s.find(i), end=' ')


def solve2798():
    read = sys.stdin.readline

    N, M = map(int, read().split())
    cards = sorted(list(map(int, read().split())), reverse=True)
    gap = M
    ans = 0
    try:
        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    tmp = cards[i] + cards[j] + cards[k]
                    if M - tmp == 0:
                        ans = tmp
                        raise
                    if tmp <= M:
                        if gap > (M - tmp):
                            gap = M - tmp
                            ans = tmp
                        break
    except:
        pass
    finally:
        print(ans)
