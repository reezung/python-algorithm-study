'''
핵심: 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.
'''
n = int(input())
r = [int(input()) for _ in range(n)]
r.sort()

result = r[0] * n
for i in range(1, n):
    if result < r[i] * (n-i):
        result = r[i] * (n-i)

print(result)
