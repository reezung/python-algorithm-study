'''
여기서는 순서가 다르면 다른 경우로 카운트함
마지막 수가 1인 경우 + 마지막 수가 2인 경우 + 마지막 수가 3인 경우

'''
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n+1):
        # 순서가 다르면 다른 경우로 카운트해야하므로, dp[i]를 계산하는데 모든 동전을 한번씩 순회
        for j in range(1, 4):
            if i-j >= 0:
                dp[i] += dp[i-j]
    print(dp[n])
