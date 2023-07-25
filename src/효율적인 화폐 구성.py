n, m = map(int, input().split())
unit_list = [int(input()) for _ in range(n)]

dp = [m + 1] * (m + 1)
for i in range(1, m + 1):
    if i in unit_list:
        dp[i] = 1
    for unit in unit_list:
        if i + unit <= m:
            dp[i + unit] = min(dp[i] + 1, dp[i + unit])

print((lambda cases: cases if cases <= m else -1)(dp[m]))
