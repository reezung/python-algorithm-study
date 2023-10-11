n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
ans = n

for i in range(n):
    if a[i] > b:
        a[i] -= b
        ans += a[i] // c
        ans += 1 if a[i] % c > 0 else 0

print(ans)
