n = list(map(int, input().split()))
n_del = set(n)  # 중복 제거

if len(n_del) == 1:
    print(10000 + n[0] * 1000)
elif len(n_del) == 2:
    same = (lambda n: n[0] if n[0] == n[1] or n[0] == n[2] else n[1])(n)
    print(1000 + same * 100)
else:
    print(max(n) * 100)
