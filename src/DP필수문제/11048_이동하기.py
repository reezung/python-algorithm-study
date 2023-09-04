'''
bfs 문제처럼 보이지만,
최단 경로가 아닌 가져올 수 있는 사탕 개수의 최댓값을 구해야 하므로
dp를 이용하는 것이 더 효율적이다.
'''
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = graph[0][0]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x in range(n):
    for y in range(m):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                dp[nx][ny] = max(dp[nx][ny], dp[x][y] + graph[nx][ny])

print(dp[n-1][m-1])