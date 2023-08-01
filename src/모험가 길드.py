n = int(input())
scare_list = list(map(int, input().split()))
scare_list.sort(reverse=True)

i, cnt = 0, 0
while i < len(scare_list):
    if n < scare_list[i]:
        i += 1
        continue
    n -= scare_list[i]
    i += scare_list[i]
    cnt += 1

print(cnt)
