N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort(reverse=True)

result = 0
repeat = 0
for _ in range(M):
    if repeat < K:
        result += num_list[0]
        repeat += 1
    else:
        result += num_list[1]
        repeat = 0

print(result)
