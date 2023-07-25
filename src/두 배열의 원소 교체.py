N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(N):
    if K <= 0:
        break
    for j in range(N):
        if B[j] > A[i]:
            A[i], B[j] = B[j], A[i]
            K -= 1
            break
print(sum(A))
