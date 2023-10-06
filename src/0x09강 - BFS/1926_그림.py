'''
그림의 개수, 그림 중 가장 넓은 것의 넓이를 출력하라

[함정] 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
'''
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


def bfs(x, y, cnt, graph):
    q = deque([(x, y)])
    graph[x][y] = 0
    cnt += 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0
                    cnt += 1

    return cnt


ans = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans.append(bfs(i, j, 0, graph))

print(len(ans))
if len(ans) == 0:
    print(0)
else:
    print(max(ans))
