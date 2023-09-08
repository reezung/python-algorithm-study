'''
여기서는 순서가 다르면 다른 경우로 카운트함
'''
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [1] * (n + 1)
    if n >= 2:  # 양수라고 했으므로, n==1일 수 있음
        dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[n])
