x = int(input())

dp = [x] * (x+1)
dp[0], dp[1] = 0, 0
for i in range(1, x):
    if i + 1 <= x:
        dp[i+1] = min(dp[i+1], dp[i] + 1)
    if i * 2 <= x:
        dp[i*2] = min(dp[i*2], dp[i] + 1)
    if i * 3 <= x:
        dp[i*3] = min(dp[i*3], dp[i] + 1)
    if i * 5 <= x:
        dp[i*5] = min(dp[i*5], dp[i] + 1)

print(dp[x])
