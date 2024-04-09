'''
몇번째 요소와 몇번째 요소를 더해서 i번째 변의 길이가 되는지
써보면서 규칙 찾기!
'''
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [1]*(n+1)
    dp[0] = 0
    if n >= 4:
        dp[4] = 2
    for i in range(5, n+1):
        dp[i] = dp[i-1] + dp[i-5]

    print(dp[n])