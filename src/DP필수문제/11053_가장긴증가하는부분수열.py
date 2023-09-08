'''
부분수열이 꼭 a[0]으로 시작하지 않을 수 있음.
bottom-up
dp[i]는 a[i]로 끝나는 부분수열의 개수를 의미
a[i]보다 작은 수가 i번째 앞에 있을경우에만 비교 후 dp값을 업데이트
'''
n = int(input())
a = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))