'''
모든 집을 칠하는 비용의 최솟값
* 1번 집의 색 != 2번 집의 색
* n번 집의 색 != (n-1)번 집의 색
* i번 집의 색 != i-1번과 i+1번 집의 색
'''
n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0] = [i for i in score[0]]

for i in range(1, n):
    for j in range(3):
        dp[i][j] = min(dp[i - 1][(j - 1) % 3], dp[i - 1][(j - 2) % 3]) + score[i][j]

print(min(dp[n-1]))
