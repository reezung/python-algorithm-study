K, N, M = map(int, input().split())
print((lambda a, b, c: 0 if a * b - M <= 0 else a * b - M)(K, N, M))
