'''
얻을 수 있는 총 점수의 최댓값을 구하는 문제.
* 연속된 세 개의 계단을 모두 밟아서는 안된다.
    => dp[i] = max(dp[i-2]+score[i], dp[i-3]+score[i-1]+score[i])
* 한번에 한 계단 또는 두 계단씩 오를 수 있다.
* 마지막 도착 계단은 반드시 밟아야 한다.
'''
n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)
dp[1] = stairs[1]

if 2 <= n:
    dp[2] = stairs[1] + stairs[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[n])

