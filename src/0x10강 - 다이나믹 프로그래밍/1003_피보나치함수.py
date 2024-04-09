t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[0]*2 for _ in range(n+1)]
    dp[0] = [1, 0]
    if n >= 1:
        dp[1] = [0, 1]
    for i in range(2, n + 1):
        dp[i] = (lambda a, b: [a[0] + b[0], a[1] + b[1]])(dp[i - 1], dp[i - 2])
    print(*dp[-1])
