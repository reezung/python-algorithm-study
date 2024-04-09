n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*i for i in range(1,n+1)]
dp[0] = board[0]

for i in range(n-1):
    for j in range(i+1):
        for t in [j, j+1]:
            dp[i+1][t] = max(dp[i+1][t], board[i+1][t]+dp[i][j])


print(max(dp[-1]))