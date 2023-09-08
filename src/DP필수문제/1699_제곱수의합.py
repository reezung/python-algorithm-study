'''
n을 제곱수의 합으로 표현할 때, 그 항의 최소 개수
dp[i+j**2] = min(dp[i] + 1, dp[i-j**2]) 하면 시간초과 발생
할당하는데 시간이 추가로 들기 때문인듯
'''
INF = int(1e9)
n = int(input())
dp = [INF] * (n+1)
dp[0] = 0

for i in range(n+1):
    for j in range(1, n+1):
        if i+j**2 > n:
            break
        if dp[i+j**2] > dp[i] + 1:
            dp[i+j**2] = dp[i] + 1

print(dp[n])
