s = list(map(int, input()))

curr = s[0]
cnt = 1

for num in s:
    if num != curr:
        cnt += 1
        curr = num

print(cnt // 2)
