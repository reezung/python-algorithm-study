'''
존재하는 블럭들만 move
- 존재하는 블럭을 체크할 때, 행/열을 체크하는 순서가 i에 따라 달랐음
- 블럭이 합쳐질 때까지 or 벽/합쳐질 수 없는 숫자를 만날 때까지 move
'''
from collections import deque
import copy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def move(x, y, b, integrated, d):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while 0 <= x + dx[d] < n and 0 <= y + dy[d] < n:
        nx = x + dx[d]
        ny = y + dy[d]
        if b[nx][ny] == 0:
            b[nx][ny] = b[x][y]
            b[x][y] = 0
            x = nx
            y = ny
        elif b[nx][ny] == b[x][y] and integrated[nx][ny] == 0:
            b[nx][ny] *= 2
            integrated[nx][ny] = 1
            b[x][y] = 0
        else:
            return b
    return b


def bfs(b):
    q = deque([b, 0])
    v = [b]
    range_x = [range(n), range(n - 1, -1, -1), range(n), range(n)]
    range_y = [range(n), range(n), range(n), range(n - 1, -1, -1)]

    max_num = max(max(i) for i in b)
    while q:
        blocks = q.popleft()
        cnt = q.popleft()
        if cnt == 5:
            break

        for i in range(4):
            b = copy.deepcopy(blocks)
            integrated = [[0] * n for _ in range(n)]

            for x in range_x[i]:
                for y in range_y[i]:
                    if b[x][y] != 0:
                        move(x, y, b, integrated, i)
            if b not in v:
                q.append(b)
                q.append(cnt + 1)
                v.append(b)
                t = max(max(i) for i in b)
                if t > max_num:
                    max_num = t

    return max_num


print(bfs(board))
