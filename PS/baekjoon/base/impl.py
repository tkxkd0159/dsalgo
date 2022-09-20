def solve1157():
    i = input().upper()
    n = 0
    c = ""
    for p in map(chr, range(65, 91)):  # A - Z
        q = i.count(p)
        if q > n:
            n, c = q, p
        elif q == n:
            c = "?"
    print(c)
