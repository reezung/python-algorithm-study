n = int(input())
A = list(map(int, input().split()))
b, c = map(int, input().split())


def ceil(num):
    if num * 10 % 10 > 0:
        return int(num) + 1
    return int(num)


ans = 0
for a in A:
    if a > 0:
        ans += 1
        a -= b
    if a > 0:
        ans += ceil(a / c)
print(ans)
