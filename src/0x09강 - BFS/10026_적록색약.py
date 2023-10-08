from collections import deque
import copy

n = int(input())
board = [list(input()) for _ in range(n)]
board_rg = copy.deepcopy(board)

for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board_rg[i][j] = 'R'


def bfs(x, y, visited, board):
    q = deque([(x, y)])
    visited[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and board[nx][ny] == board[x][y]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1


def area_num(board):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                cnt += 1
                bfs(i, j, visited, board)
    print(cnt, end=' ')


area_num(board)
area_num(board_rg)
