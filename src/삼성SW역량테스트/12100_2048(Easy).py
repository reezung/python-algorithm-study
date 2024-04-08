'''
존재하는 블럭들만 move
- 존재하는 블럭을 체크할 때, 행/열을 체크하는 순서가 i에 따라 달랐음
- 이미 합쳐진 블럭을 한번 더 합치면 안됨
- 완전탐색!
'''
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
range_x = [range(1, n), range(n - 2, -1, -1), range(n), range(n)]
range_y = [range(n), range(n), range(1, n), range(n - 2, -1, -1)]


def deepcopy(list):
    nlist = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            nlist[x][y] = list[x][y]
    return nlist


def move(blocks, i):
    integrated = []
    for x in range_x[i]:
        for y in range_y[i]:
            if blocks[x][y] != 0:
                block = blocks[x][y]
                blocks[x][y] = 0
                nx = x
                ny = y
                while True:
                    nx += dx[i]
                    ny += dy[i]
                    if not (0 <= nx < n and 0 <= ny < n):
                        break
                    if blocks[nx][ny] == block and (nx, ny) not in integrated:
                        integrated.append((nx, ny))
                        nx += dx[i]
                        ny += dy[i]
                        break
                    elif blocks[nx][ny] != 0:
                        break
                nx -= dx[i]
                ny -= dy[i]
                blocks[nx][ny] += block


def dfs(board, i):
    global ans
    nboard = deepcopy(board)
    move(nboard, i)

    if len(s) == 5:
        ans = max(ans, max([max(b) for b in nboard]))
        return

    for i in range(4):
        s.append(i)
        dfs(nboard, i)
        s.pop()


s = []
ans = 0
for i in range(4):
    s.append(i)
    dfs(board, i)
    s.pop()

print(ans)
