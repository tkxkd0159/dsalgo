my_map = [
    [4, 3, 2, 1],
    [0, 0, 0, 0],
    [0, 0, 9, 0],
    [1, 2, 3, 4]
]

from collections import deque

INF = int(1e9)
dx = [-1, 1, 0, 0]  # up, down
dy = [0, 0, -1, 1]  # left, right

total_time = 0
ate = 0
now_size = 2
now_x, now_y = 0, 0
N = len(my_map)
for i in range(N):
    for j in range(N):
        if my_map[i][j] == 9:
            now_x, now_y = i, j
            my_map[i][j] = 0


def bfs():
    dist = [[-1] * N for _ in range(N)]
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]
            if 0 <= nx < N and 0 <= ny < N:
                if dist[nx][ny] == -1 and my_map[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist


def find(dist):
    min_dist = INF
    x, y = 0, 0
    for ii in range(N):
        for jj in range(N):
            if dist[ii][jj] != -1 and 1 <= my_map[ii][jj] < now_size:
                if dist[ii][jj] < min_dist:
                    min_dist = dist[ii][jj]
                    x, y = ii, jj

    if min_dist == INF:
        return None
    else:
        return x, y, min_dist


if __name__ == "__main__":
    while True:
        value = find(bfs())
        if value is None:
            print(total_time)
            break

        now_x = value[0]
        now_y = value[1]
        total_time += value[2]
        ate += 1
        my_map[now_x][now_y] = 0
        if ate >= now_size:
            now_size += 1
            ate = 0

    map1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 9, 0],
    ]
    map2 = [
        [0, 0, 1],
        [0, 0, 0],
        [0, 9, 0],
    ]
    map3 = [
        [4, 3, 2, 1],
        [0, 0, 0, 0],
        [0, 0, 9, 0],
        [1, 2, 3, 4]
    ]
