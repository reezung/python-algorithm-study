n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.reverse()

result = 0
for ai in a:
    if ai <= k:
        result += k//ai
        k %= ai

print(result)
