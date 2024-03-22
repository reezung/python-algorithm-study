from copy import deepcopy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cctvs = []
modes = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    [[0, 1, 2, 3]]
]
ans = int(1e9)

for x in range(n):
    for y in range(m):
        if graph[x][y] in [1, 2, 3, 4, 5]:
            cctvs.append((x, y, graph[x][y]))


def count_zero(map):
    result = 0
    for i in range(n):
        result += map[i].count(0)
    return result


def watch(x, y, I, map):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in I:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                break
            if map[nx][ny] == 6:
                break
            elif map[nx][ny] == 0:
                map[nx][ny] = 7


def dfs(depth, map):
    global ans
    if depth == len(cctvs):
        ans = min(ans, count_zero(map))
        return
    x, y, type = cctvs[depth]
    for mode in modes[type]:
        temp = deepcopy(map)
        watch(x, y, mode, temp)
        dfs(depth + 1, temp)


dfs(0, graph)
print(ans)
