'''
deepcopy 절대 쓰지 않기...
1. dfs -> 중복없는 조합 구하기
2. bfs -> 인접한 조합인지 여부 확인하기
'''
from collections import deque

board = [list(input()) for _ in range(5)]
idx = [(i, j) for i in range(5) for j in range(5)]
s = []
n = []
ans = 0


def is_available(l):
    q = deque([l[0]])
    l.remove(l[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in l:
                q.append((nx, ny))
                l.remove((nx, ny))
    if len(l) == 0:
        return True
    return False


def dfs(depth):
    global ans
    if len(s) == 7:
        if n.count('S') >= 4 and is_available([i for i in s]):
            ans += 1
        return
    for i in range(depth, 25):
        x, y = idx[i]
        s.append((x, y))
        n.append(board[x][y])
        dfs(i + 1)
        s.pop()
        n.pop()


dfs(0)
print(ans)
