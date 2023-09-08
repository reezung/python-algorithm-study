'''
i - j**2로 업데이트해주어야 시간초과가 나지 않음.
안쪽루프를 n번이 아닌 i번만 돌아도 되기 때문
'''
n = int(input())
dp = [i for i in range(n+1)]

for i in range(n+1):
    for j in range(1, i):
        if j**2 > i:
            break
        if dp[i] > dp[i-j**2] + 1:
            dp[i] = dp[i-j**2] + 1

print(dp[n])
