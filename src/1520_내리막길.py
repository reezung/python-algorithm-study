'''
하지만 시간초과가 발생함.
'''
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = 1

result = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(start):
    global result
    x, y = start
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[x][y] > graph[nx][ny]:
                if (nx, ny) == (n - 1, m - 1):
                    result += 1
                dfs((nx, ny))


dfs((0, 0))
print(result)