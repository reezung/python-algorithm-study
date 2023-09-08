'''
동전 개수의 합이 n으로 정해져있으므로 개수를 기준으로 dp를 생성
'''
n = int(input())
p = [0]+list(map(int, input().split()))
dp = [i for i in p]
for i in range(1, n+1):
    for j in range(1, n+1):
        if 1<= i+j <= n:
            dp[i+j] = max(dp[i+j], dp[i] + p[j])

print(dp[n])