'''
순서가 다르면 다른 경우로 카운트.
한개의 수를 여러번 쓸 수 있음.
dp[1][1] = dp[0][1] + dp[0][0]
dp[1][2] = dp[0][2] + dp[0][1]
dp[6][3] = dp[5][3] + dp[5][2]
dp[i-1][k] = dp[0][k-1] + ... + dp[i-1][k-1]

dp[i][k] = dp[0][k-1] + ... + dp[i][k-1]
         = dp[i-1][k] + dp[i][k-1]
'''
n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[0] = [0] + [1 for _ in range(k)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[n][k] % 10 ** 9)
