from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]


def bfs(graph, start):
    visited = [False] * len(graph)
    seq = []
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        seq.append(v)
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return seq


print(bfs(graph, 1))
