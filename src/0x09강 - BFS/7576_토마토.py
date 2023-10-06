'''
창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소일수

[함정]
- 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다
- 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력
- 토마토가 모두 익지는 못하는 상황이면 -1을 출력
'''
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            if graph[i][j] == 1:
                q.append((i, j))
            visited[i][j] = 1

if sum([sum(v) for v in visited]) == n * m:
    print(0)
    exit(0)


def bfs():
    global visited, q
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


bfs()
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            print(-1)
            exit(0)

print(max([max(v) for v in visited]) - 1)
