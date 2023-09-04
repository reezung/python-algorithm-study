'''
ex) 길이 3이고 3으로 끝나는 계단수의 개수
(길이 2이고 2로 끝나는) + (길이 2이고 4로 끝나는) 계단수의 합
'''
n = int(input())
dp = [[1] * 10 for _ in range(n + 1)]
dp[1][0] = 0

for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][1]
    for j in range(1, 9):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
    dp[i][9] = dp[i - 1][8]

print(sum(dp[n]) % 10 ** 9)
