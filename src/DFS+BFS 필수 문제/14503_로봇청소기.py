'''
우선적으로 탐색하는 방향 순서 중요
'''
from collections import deque
n, m = map(int, input().split())
# d: 0(북), 1(동), 2(남), 3(서)
start = tuple(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]
graph[start[0]][start[1]] = -1
cnt = 1

def bfs(v):
    global cnt
    q = deque([v])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x, y, d = q.popleft()
        for _ in range(4):
            d = (d - 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = -1
                    cnt += 1
                    q.append((nx, ny, d))
                    break

        if not q:
            nd = (d + 2) % 4
            nx = x + dx[nd]
            ny = y + dy[nd]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    print(cnt)
                    exit(0)
                else:
                    # graph[nx][ny] == -1인 경우
                    q.append((nx, ny, d))



bfs(start)


