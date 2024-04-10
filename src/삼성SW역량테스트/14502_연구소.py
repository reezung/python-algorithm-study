from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
walls = []

s = []


def dfs(depth):
    if len(s) == 3:
        walls.append([*s])
        return

    for i in range(depth, n * m):
        x, y = i // m, i % m
        if board[x][y] == 0:
            s.append((x, y))
            dfs(x * m + y + 1)
            s.pop()


def bfs(nboard, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(x, y)])
    nboard[x][y] = -1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and nboard[nx][ny] != -1:
                if nboard[nx][ny] == 0:
                    q.append((nx, ny))
                    nboard[nx][ny] = -1


def deepcopy(list):
    nlist = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            nlist[i][j] = list[i][j]
    return nlist


dfs(0)

for w in walls:
    nboard = deepcopy(board)
    for i in w:
        x, y = i
        nboard[x][y] = 1
    for i in range(n):
        for j in range(m):
            if nboard[i][j] == 2:
                bfs(nboard, i, j)
    ans = max(ans, sum([b.count(0) for b in nboard]))

print(ans)
