import sys
read = sys.stdin.readline

class DFS:
    def __init__(self) -> None:
        pass


class BFS:
    def __init__(self) -> None:
        pass


class BruteForce:
    def __init__(self) -> None:
        pass

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def solve2231():
        def gen(n):
            res = n
            while n > 0:
                res += (n % 10)
                n = n//10
            return res
        N = int(input().strip())
        isFind = False
        offset = 54
        for i in range(max(1, N - offset), N):
            tmp = gen(i)
            if tmp == N:
                print(i)
                isFind = True
                break
        if not isFind:
            print(0)

    @staticmethod
    def solve1436():
        N = int(input())
        cnt = 0
        i = 0
        while True:
            snum = f'{i}666'
            dupsix = 0
            for j in range(len(snum)-3):
                if snum[-4-j] == '6':
                    dupsix += 1
                else:
                    break
            cnt += (10**dupsix)
            if cnt >= N:
                if dupsix == 0:
                    print(int(snum))
                    break
                else:
                    cnt -= (10**dupsix)
                    print(int(snum) - (int(snum) % (10**dupsix)) + (N-cnt-1))
                    break
            else:
                i += 1

class BianrySearch:
    def __init__(self) -> None:
        pass

    @staticmethod
    def solve1920():
        def bin(n, arr):
            start = 0
            end = len(arr) - 1

            while start <= end:
                mid = (start + end) // 2

                if arr[mid] == n:
                    return 1
                elif arr[mid] < n :
                    start = mid + 1
                else:
                    end = mid -1
            return 0

        N = int(read())
        l = list()
        for i in map(int, read().split()):
            l.append(i)
        l.sort()
        M = int(read())
        for i in map(int, read().split()):
            print(bin(i, l))
    
    @staticmethod
    def solve1654():
        K, N = map(int, read().split())
        l = []
        for _ in range(K):
            l.append(int(read()))
        
        low = 1
        high = max(l)
        cached = 0
        
        while low <= high:
            mid = (low + high) // 2
            tot = 0
            for elem in l:
                tot += (elem // mid)
            
            if tot >= N:
                cached = mid
                low = mid + 1
            else:
                high = mid - 1
        print(cached)
        