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


seq = []
visited = [False] * 9


def dfs_wo_stack(graph, v, visited):
    visited[v] = True
    seq.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs_wo_stack(graph, i, visited)


dfs_wo_stack(graph, 1, visited)
print(seq)


def dfs(graph: list[list], start):
    visited = [False] * len(graph)
    stack = []
    seq = []

    stack.append(start)
    while stack:
        node = stack.pop()
        if not visited[node]:
            seq.append(node)
            visited[node] = True
            stack.extend(graph[node][::-1])
    return seq


print(dfs(graph, 1))
