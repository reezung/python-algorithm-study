from collections import deque

while True:
    l, r, c = map(int, input().split())
    if (l, r, c) == (0, 0, 0):
        break
    graph = []
    for z in range(l):
        graph.append([list(input()) for _ in range(r)])
        input()

    s = tuple()
    for z in range(l):
        if not s:
            for x in range(r):
                if not s:
                    for y in range(c):
                        if graph[z][x][y] == 'S':
                            s = (z, x, y, 0)
                            break
    q = deque([s])
    ans = "Trapped!"
    dz = [0, 0, 0, 0, -1, 1]
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    while q and ans == "Trapped!":
        z, x, y, cnt = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                if graph[nz][nx][ny] == 'E':
                    ans = f"Escaped in {cnt + 1} minute(s)."
                    break
                elif graph[nz][nx][ny] == '.':
                    q.append((nz,nx, ny, cnt+1))
                    graph[nz][nx][ny] = 'S'
    print(ans)
