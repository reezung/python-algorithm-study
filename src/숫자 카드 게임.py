N, M = map(int, input().split())
min_card = [min(map(int, input().split())) for _ in range(N)]
print(max(min_card))
