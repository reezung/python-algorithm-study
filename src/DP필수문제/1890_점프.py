'''
메모리 제한이 128MB로, deque를 사용하는 bfs를 사용하면 메모리 초과가 뜬다.
전 단계의 최단경로 수를 이용하는 dp를 이용하면 빠르게 풀 수 있다.
'''
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]    # 경로의 개수
dp[0][0] = 1

dx = [1, 0]
dy = [0, 1]

for x in range(n):
    for y in range(n):
        if graph[x][y] != 0:
            for i in range(2):
                nx = x + graph[x][y] * dx[i]
                ny = y + graph[x][y] * dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    dp[nx][ny] += dp[x][y]
                    
print(dp[n - 1][n - 1])