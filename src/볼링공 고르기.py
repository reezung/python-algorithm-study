n, m = map(int, input().split())
ball = list(map(int, input().split()))
weight = [0] * (m + 1)

for b in ball:
    weight[b] += 1


def combination(n, k):
    return n * (n - 1) // k


result = combination(n, 2)
for w in weight:
    if w > 1:
        result -= combination(w, 2)

print(result)
