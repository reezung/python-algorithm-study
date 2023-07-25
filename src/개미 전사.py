n = int(input())
food_list = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = food_list[1]

for i in range(2, n+1):
    dp[i] = max(dp[i-2] + food_list[i], dp[i-1])

print(dp[n])

