n = int(input())
units = list(map(int, input().split()))
units.sort(reverse=True)

for price in range(1, sum(units)):
    temp = price
    for unit in units:
        if temp >= unit:
            temp -= unit
    if temp > 0:
        print(price)
        exit()

print(sum(units)+1)

