import copy

my_map = [[] for _ in range(4)]   # (number, direction)

# for i in range(4):
#     tmp = list(map(int, input().split()))
#     for j in range(0, 7, 2):
#         my_map[i].append([tmp[j], tmp[j+1]-1])
my_map = [[[7, 5], [2, 2], [15, 5], [9, 7]],
          [[3, 0], [1, 7], [14, 6], [10, 0]],
          [[6, 0], [13, 5], [4, 2], [11, 3]],
          [[16, 0], [8, 6], [5, 1], [12, 1]]]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]  # 북쪽부터 반시계 방향
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def turn_left(direction):
    return (direction + 1) % 8


def find_fish(mm, number):
    for ii in range(4):
        for jj in range(4):
            if mm[ii][jj][0] == number:
                return ii, jj
    return None


def move_all_fish(mm, now_x, now_y):
    for ii in range(1, 17):
        pos = find_fish(mm, ii)
        if pos is not None:
            x, y = pos[0], pos[1]
            direction = mm[x][y][1]
            for jj in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == now_x and ny == now_y):
                        mm[x][y][1] = direction
                        mm[x][y], mm[nx][ny] = mm[nx][ny], mm[x][y]
                        break
                direction = turn_left(direction)


def get_possible_shark(mm, now_x, now_y):
    target_pos = []
    direction = mm[now_x][now_y][1]
    for ii in range(4):
        now_x += dx[direction]
        now_y += dy[direction]

        if 0 <= now_x < 4 and 0 <= now_y < 4:
            if mm[now_x][now_y][0] != -1:
                target_pos.append((now_x, now_y))

    return target_pos


result = 0
def dfs(my_map, now_x, now_y, total):
    global result
    mm = copy.deepcopy(my_map)
    total += mm[now_x][now_y][0]
    mm[now_x][now_y][0] = -1

    move_all_fish(mm, now_x, now_y)
    target_pos = get_possible_shark(mm, now_x, now_y)
    if len(target_pos) == 0:
        result = max(result, total)
        return

    for pos in target_pos:
        dfs(mm, pos[0], pos[1], total)


dfs(my_map, 0, 0, 0)
print(result)
