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
