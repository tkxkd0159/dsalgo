def solve4673():
    def generator(x):
        tot = x
        while x > 0:
            tot += (x % 10)
            x = x // 10
        return tot

    N = 10001
    self_num = [True] * N
    for i in range(1, N):
        cur = generator(i)
        if cur == 9914:
            print(i)
        if cur > 10000:
            continue
        self_num[cur] = False

    for i, val in enumerate(self_num):
        if i == 0:
            continue
        if val == True:
            print(i)


def solve1018():
    M, N = map(int, input().rstrip().split())
    cmap = []
    for i in range(M):
        cmap.append(input().rstrip())
    S = 8
    min_ = 32
    for i in range(M - S + 1):
        for j in range(N - S + 1):
            tmp = 0
            for k in range(i, i+S):
                for l in range(j, j+S):
                    if cmap[k][l] != ("B" if (k+l) % 2 == 0 else "W"):
                        tmp += 1

            if tmp > 32:
                min_ = min(min_, 64-tmp)
            else:
                min_ = min(min_, tmp)
    print(min_)
