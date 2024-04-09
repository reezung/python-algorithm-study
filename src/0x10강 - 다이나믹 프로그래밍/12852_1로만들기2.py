n = int(input())
dp = [int(1e9)]*(n+1)
ans = [[] for _ in range(n+1)]
dp[1] = 0
ans[1] = [1]

for i in range(1, n+1):
    for target in [i+1, i*2, i*3]:
        if target <= n and dp[i]+1 < dp[target]:
            dp[target] = dp[i]+1
            ans[target] = [target] + ans[i]

print(dp[-1])
print(*ans[-1])
