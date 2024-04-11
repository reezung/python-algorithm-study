n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cctvs = []
cctvs_d = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [3, 1], [1, 2], [2, 0]],
    [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]],
    [[0, 1, 2, 3]]
]
ans = int(1e9)

# 북, 남, 서, 동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x in range(n):
    for y in range(m):
        if board[x][y] in range(1, 6):
            cctvs.append((x, y))


def deepcopy(list):
    nlist = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            nlist[i][j] = list[i][j]
    return nlist


def cctv(board, i, x, y):
    x += dx[i]
    y += dy[i]
    if 0 <= x < n and 0 <= y < m:
        if board[x][y] == 6:
            return
        if board[x][y] == 0:
            board[x][y] = '#'
        cctv(board, i, x, y)


s = []


def dfs(depth):
    global ans

    if len(s) == len(cctvs):
        nboard = deepcopy(board)
        for c in s:
            ilist, x, y = c
            for i in ilist:
                cctv(nboard, i, x, y)
        ans = min(ans, sum([b.count(0) for b in nboard]))
        return

    for cctv_i in range(depth, len(cctvs)):
        x, y = cctvs[cctv_i]
        type = board[x][y]
        for ilist in cctvs_d[type]:
            s.append((ilist, x, y))
            dfs(cctv_i + 1)
            s.pop()


dfs(0)
print(ans)
