class Normal:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def solve11650():      # easy
        N = int(input())
        coord = []
        for _ in range(N):
            coord.append(list(map(int, input().split())))
        xysort = sorted(coord, key=lambda x: (x[0], x[1]))
        for x, y in xysort:
            print(x, y)