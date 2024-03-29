# This is coding test
class Greedy:
    def __init__(self):
        pass

    @staticmethod
    def change(n):
        count = 0
        coin_types = [500, 100, 50, 10]
        for c in coin_types:
            count += n // c
            n %= c

        return count

    @staticmethod
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

    @staticmethod
    def num_cardgame():
        h, w = map(int, input().split())
        res = []
        for _ in range(h):
            res.append(min(list(map(int, input().split()))))

        return max(res)

    @staticmethod
    def to_one(n, k, case):
        cnt = 0

        if case == 1:
            while (n != 1):
                if n % k == 0:
                    n /= k
                    cnt += 1
                else:
                    n -= k
                    cnt += 1

        if case == 2:
            while True:
                target = (n // k) * k
                cnt += (n - target)
                n = target

                if n < k:
                    break
                cnt += 1
                n //= k

            cnt += (n - 1)

        return cnt

class Implementations:
    def __init__(self) -> None:
        pass

    @staticmethod
    def udlr(n, path, case):
        """
        Args:
            n (int): the size of map
            path (list): sequences of moving
        """
        limit = [1, n]
        coord = [1, 1]

        if case == 'mine':
            for do_ in path:
                if do_ == 'D':
                    coord[0] += 1
                    if coord[0] > limit[1]:
                        coord[0] -= 1

                elif do_ == 'U':
                    coord[0] -= 1
                    if coord[0] < limit[0]:
                        coord[0] += 1

                elif do_ == 'L':
                    coord[1] -= 1
                    if coord[1] < limit[0]:
                        coord[1] += 1

                elif do_ == 'R':
                    coord[1] += 1
                    if coord[1] > limit[1]:
                        coord[1] -= 1

        elif case == 'solution':
            dx = [0, 0, -1, 1]
            dy = [-1, 1, 0, 0]
            move_types = ['L', 'R', 'U', 'D']
            for do_ in path:
                for i in range(len(move_types)):
                    if do_ == move_types[i]:
                        nx = coord[0] + dx[i]
                        ny = coord[1] + dy[i]
                if nx < limit[0] or ny < limit[0] or nx > limit[1] or ny > limit[1]:
                    continue

                coord[0], coord[1] = nx, ny

        return coord

    def clock(h, case):
        """Find time who include '3' its time

        Args:
            n (int): 00:00:00 to N:59:59
        """
        if case == 1:
            incl3_hour = [3, 13, 23]
            incl_3 = 5 * 1 + 10
            not_3 = 60 - incl_3
            under_min_case = incl_3 * not_3 * 2 + incl_3 * incl_3

            res = 0
            for i in range(h + 1):
                if i in incl3_hour:
                    res += 3600
                else:
                    res += under_min_case

        elif case == 2:
            res = 0
            for i in range(h + 1):
                for j in range(60):
                    for k in range(60):
                        if '3' in str(i) + str(j) + str(k):
                            res += 1

        return res

    def knight_of_royal(pos): # c2 : 6, a1 : 2

        conv_char = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
        res = 0
        x, y = conv_char[pos[0]], int(pos[1])
        limit = [1, 8]
        move_type = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

        for dx, dy in move_type:
            nx = x + dx
            ny = y + dy
            if nx < limit[0] or ny < limit[0] or nx > limit[1] or ny > limit[1]:
                continue
            else:
                res += 1
        return res


    def grid_game(map_size, character, map):
        # test case
        # Implementations.grid_game([4, 4], [1, 1, 0], [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]])
        y, x = character[0], character[1]
        direction = character[2]
        mymap = map
        mymap[y][x] = 2

        move_type = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        cnt = 0
        move_sig = False
        dir_seq = [0, 3, 2, 1]
        while True:
            for i in range(1, 5):
                nx = x + move_type[-i+direction][1]
                ny = y + move_type[-i+direction][0]
                idx = dir_seq.index(direction)

                if mymap[ny][nx] != 1 and mymap[ny][nx] != 2:
                    x = nx
                    y = ny
                    direction = dir_seq[(idx + i) % 4]
                    move_sig = True
                    mymap[ny][nx] = 2
                    cnt += 1
                    break

            if not move_sig:
                idx = dir_seq.index(direction)
                print(type(idx))
                nx = x + move_type[(idx + 2) % 4][1]
                ny = y + move_type[(idx + 2) % 4][0]
                if mymap[ny][nx] == 1:
                    break
                else:
                    x = nx
                    y = ny
                    cnt += 1

            move_sig = False

        return cnt


