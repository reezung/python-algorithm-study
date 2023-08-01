food_times = list(map(int, input().split()))
k = int(input())

i = 0
for _ in range(k):
    if sum(food_times) == 0:
        print(-1)
        break
    while food_times[i] <= 0:
        i = (i + 1) % 3
    food_times[i] -= 1
    i = (i + 1) % 3

print(i+1)
