inp = list(map(int, input()))

if inp[0] == 1:
    print(1, end="")

x = 0
while x < len(inp):
    cnt = 0
    for i in inp[x + 1:]:
        if inp[x] == i:
            cnt += 1
        else:
            break
    if cnt >= 25:
        print('Z', end="")
    else:
        print(chr(ord('A') + cnt), end="")
    x += cnt + 1


