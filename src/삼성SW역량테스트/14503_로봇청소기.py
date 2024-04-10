n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0


def move(x, y, d):
    global cnt

    if board[x][y] == 0:
        board[x][y] = 2
        cnt += 1

    for _ in range(4):
        d = (d - 1) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            move(nx, ny, d)
            return

    nx = x - dx[d]
    ny = y - dy[d]
    if 0 <= nx < n and 0 <= ny < m:
        if board[nx][ny] == 1:
            return
        move(nx, ny, d)


move(r, c, d)
print(cnt)
