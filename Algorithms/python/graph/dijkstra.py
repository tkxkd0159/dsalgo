def getSmallestNode(n, d, v):
    min_v = int(1e9)
    index = 0
    for i in range(1, n + 1):
        if d[i] < min_v and not v[i]:
            min_v = d[i]
            index = i
    return index

def dijkstraSlow(n, start, d, v, g):
    d[start] = 0
    v[start] = True

    for j in g[start]:
        d[j[0]] = j[1]

    from_node = [0] * (n+1)
    from_node[1] = 1
    from_cost = [1e9] * (n+1)
    for idx, j in enumerate(g):
        for end, cost in j:
            if cost < from_cost[end]:
                from_node[end] = idx
                from_cost[end] = cost

    for _ in range(n-1):
        now = getSmallestNode(n, d, v)
        v[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for next, n_cost in g[now]:
            cost = d[now] + n_cost
            if cost < d[next]:
                d[next] = cost
                from_node[next] = now


    return from_node

def printShortestCost(start, distance):
    print("\n * Show cost for all nodes")
    for i, cost in enumerate(distance):
        if i == 0:
            continue
        if cost == int(1e9):
            print("INFINITY")
        print(f'{start} -> {i} : {cost}')

def printTrace(start, trace):
    def recurTrace(start, node, trace):
        if trace[node] == start:
            print(f'{start} -> ', end='')
            return
        else:
            recurTrace(start, trace[node], trace)
            print(f'{trace[node]} -> ', end='')

    print(f'\n * Show all shortest path from {start}')
    for i in range(1, len(trace)):
        print(f'{start} -> {i} : ', end='')
        recurTrace(start, i, trace)
        print(f'{i}')


if __name__ == "__main__":
    INF = int(1e9)
    n, edge = 6, 11
    start = 1
    # graph = [[] for _ in range(n + 1)]
    graph = [
            [],
            [(2, 2), (3, 5), (4, 1)],  # start : (end cost)
            [(3, 3), (4, 2)],
            [(2, 3), (6, 5)],
            [(3, 3), (5, 1)],
            [(3, 1), (6, 2)],
            []
            ]
    visited = [False] * (n+1)
    dist = [INF] * (n+1)

    p_trace = dijkstraSlow(n, start, dist, visited, graph)
    printTrace(start, p_trace)
    printShortestCost(start, dist)
