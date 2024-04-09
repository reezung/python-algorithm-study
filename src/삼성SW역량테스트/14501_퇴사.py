n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)

for i in range(n):
    t, p = board[i]
    for j in range(i+t, n+1):
        dp[j] = max(dp[i]+p, dp[j])

print(dp[-1])