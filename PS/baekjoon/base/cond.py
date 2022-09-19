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
