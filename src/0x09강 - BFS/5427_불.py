from collections import deque

t = int(input())


def bfs(s, F, w, h, board):
    q = deque()
    for f in F:
        q.append((f[0], f[1], -1))
    q.append((s[0], s[1], 0))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, cnt = q.popleft()

        if cnt != -1 and (x in [0, h - 1] or y in [0, w - 1]):
            return cnt + 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if cnt == -1 and board[nx][ny] in ['.', '@']:
                    q.append((nx, ny, -1))
                    board[nx][ny] = '*'
                elif cnt > -1 and board[nx][ny] == '.':
                    q.append((nx, ny, cnt + 1))
                    board[nx][ny] = '@'
    return 'IMPOSSIBLE'


for _ in range(t):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    s = (0, 0)
    f = []

    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                s = (i, j)
            elif board[i][j] == '*':
                f.append((i, j))
    print(bfs(s, f, w, h, board))
