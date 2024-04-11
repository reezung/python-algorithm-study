from collections import deque

gears = [list(map(int, input())) for _ in range(4)]
k = int(input())
rotation = [list(map(int, input().split())) for _ in range(k)]


def rotate(i, d):
    if d == 1:
        gears[i] = gears[i][7:] + gears[i][:7]
    else:
        gears[i] = gears[i][1:] + gears[i][:1]


for i in range(k):
    n, d = rotation[i]
    n -= 1

    contact = []
    for j in range(3):
        if gears[j][2] == gears[j + 1][6]:
            contact.append(False)
        else:
            contact.append(True)

    q = deque([(n, d)])
    visited = [n]
    while q:
        n, d = q.popleft()
        rotate(n, d)
        if 0 <= n - 1 < 4:
            if contact[n - 1] and n-1 not in visited:
                q.append((n - 1, -1 * d))
                visited.append(n-1)
        if 0 <= n + 1 < 4:
            if contact[n] and n+1 not in visited:
                q.append((n + 1, -1 * d))
                visited.append(n + 1)

ans = 0
for i in range(4):
    if gears[i][0] == 1:
        ans += 2 ** i

print(ans)
