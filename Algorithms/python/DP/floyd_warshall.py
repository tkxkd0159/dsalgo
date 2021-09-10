INF = int(1e9)

n, edge = 4, 7
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

costs = [[1, 2, 4], [1, 4, 6], [2, 1, 3], [2, 3, 7], [3, 1, 5], [3, 4, 4], [4, 3, 2]]

for i, j, cost in costs:
    graph[i][j] = cost

for k in range(1, n + 1):
    for i in range(1, n + 1):
        if i == k:
            continue
        for j in range(1, n + 1):
            if j == k:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end=" ")
        if j == n:
            print("")