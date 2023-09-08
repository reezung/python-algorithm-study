'''
k원이 되도록 하는 동전 조합의 최소 개수
coin의 종류가 주어지고, 각 종류의 동전을 몇개라도 사용가능
dp[i]에 i원이 되도록 하는 동전 조합의 최소 개수를 저장
합이 k원으로 정해져있다면 합을 dp의 인덱스로 두기
'''
INF = int(1e9)
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [INF] * (k+1)
for c in coins:
    if 1 <= c <= k:
        dp[c] = 1

for i in range(1, k+1):
    if dp[i] == INF:
        continue
    for j in range(n):
        if 1 <= i+coins[j] <= k:
            dp[i+coins[j]] = min(dp[i]+1, dp[i+coins[j]])

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])


