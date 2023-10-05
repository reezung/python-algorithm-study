from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

icon = ['|', '-']
dx = [1, 0]
dy = [0, 1]


def bfs(sx, sy, i):
    global visited
    q = deque([(sx, sy)])
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            if board[nx][ny] == icon[i]:
                q.append((nx, ny))
                visited[nx][ny] = 1


cnt = 0
for x in range(n):
    for y in range(m):
        if visited[x][y] == 0:
            cnt += 1
            if icon[0] == board[x][y]:
                bfs(x, y, 0)
            else:
                bfs(x, y, 1)

print(cnt)
