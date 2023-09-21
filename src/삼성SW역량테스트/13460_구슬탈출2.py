'''
bfs에서 방문 체크는 '큐에 삽입하는 순간' 해야함
'''
from collections import deque
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

rx, ry, bx, by = 0, 0, 0, 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(x, y, d):
    cnt = 0
    while board[x][y] != 'O' and board[x+dx[d]][y+dy[d]] != '#':
        x += dx[d]
        y += dy[d]
        cnt += 1
    return x, y, cnt


def bfs(rx, ry, bx, by):
    q = deque([(rx, ry, bx, by, 1)])
    visited = [(rx, ry, bx, by)]    # 파란 구슬의 위치도 방문 체크에 포함해야함
    while q:
        rx, ry, bx, by, cnt = q.popleft()

        if cnt > 10:
            break

        for i in range(4):
            nrx, nry, rCnt = move(rx, ry, i)
            nbx, nby, bCnt = move(bx, by, i)

            if board[nbx][nby] == 'O':
                continue

            if board[nrx][nry] == 'O':
                return cnt

            if (nrx, nry) == (nbx, nby):
                if rCnt > bCnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx, nry, nbx, nby) not in visited:
                visited.append((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, cnt + 1))
    return -1


print(bfs(rx, ry, bx, by))
