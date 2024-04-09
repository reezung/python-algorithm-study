n = int(input())
a = list(map(int, input().split()))
dp = [x for x in a]

for i in range(n):
    for j in range(i+1,n):
        if a[i] < a[j]:
            dp[j] = max(dp[j], dp[i]+a[j])

print(max(dp))

