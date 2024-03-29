import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [0]+list(map(int, input().split()))
for x in range(2, n+1):
    dp[x] += dp[x - 1]

for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j]-dp[i-1])