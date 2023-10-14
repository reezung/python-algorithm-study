from collections import deque

m, n, k = map(int, input().split())
board = [[0] * m for _ in range(n)]
res = []

for _ in range(k):
    ldx, ldy, rux, ruy = map(int, input().split())
    for i in range(ldx, rux):
        for j in range(ldy, ruy):
            board[i][j] = 1


def bfs(x, y):
    global board
    q = deque([(x, y)])
    board[x][y] = 1
    cnt = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    q.append((nx, ny))
                    board[nx][ny] = 1
                    cnt += 1
    res.append(cnt)

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            bfs(i, j)

print(len(res))
res.sort()
for r in res:
    print(r, end=" ")


