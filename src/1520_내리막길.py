'''
dfs + dp.
dfs만으로 풀면 시간 초과가 발생함.
방문체크를 통해 루프를 방지해주는 것이 중요.
'''
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    global dp
    if (x, y) == (m - 1, n - 1):
        return 1
    if dp[x][y] > -1:  # 방문한 적이 있다면
        return dp[x][y]
    # -1이면 방문하지 않은 경로이므로 dfs + dp 수행
    # 루프를 방지하기 위해 dp를 -1로 초기화하고, 이동할 때마다 0으로 다시 설정해줌
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[x][y] > graph[nx][ny]:
            dp[x][y] += dfs(nx, ny)  # 방문하지 않은 노드에 대해서만 dfs+dp 수행, 이미 방문한 노드는 계산된 값 가져옴.
    return dp[x][y]


print(dfs(0, 0))
