n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
d = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

up, down, front, back, left, right = 0, 0, 0, 0, 0, 0


def rotate_dice(d):
    global up, down, front, back, left, right
    temp = up
    if d == 1:  # 동
        up = left
        left = down
        down = right
        right = temp
    elif d == 2:  # 서
        up = right
        right = down
        down = left
        left = temp
    elif d == 3:  # 남
        up = front
        front = down
        down = back
        back = temp
    else:  # 북
        up = back
        back = down
        down = front
        front = temp


for i in range(k):
    x += dx[d[i]]
    y += dy[d[i]]
    if 0 <= x < n and 0 <= y < m:
        rotate_dice(d[i])
        if board[x][y] == 0:
            board[x][y] = down
        else:
            down = board[x][y]
            board[x][y] = 0
        print(up)
    else:
        x -= dx[d[i]]
        y -= dy[d[i]]
