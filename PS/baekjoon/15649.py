# N과 M
n, m = map(int, input().split())
visited = [0 for _ in range(n + 1)]
seq_arr = [0 for _ in range(m)]


def dfs(cnt):
    if cnt == m:
        for elem in seq_arr:
            print(elem, end=' ')
        print("")
        return 0

    for i in range(1, n + 1):
        if visited[i] is not True:
            visited[i] = True
            seq_arr[cnt] = i
            dfs(cnt + 1)
            visited[i] = False


dfs(0)  # 4 2
