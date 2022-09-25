class SString:
    def __init__(self) -> None:
        pass

    @staticmethod
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

    @staticmethod
    def solve15829():
        N = int(input())
        S = input()
        res = 0
        for i, s in enumerate(S):
            res += (ord(s)-96)*(31**i)
        print(res % 1234567891)
