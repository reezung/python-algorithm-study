from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
cnt = 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(graph, start):
    queue = deque([start])
    graph[start[0]][start[1]] = 1
    while queue:
        v = queue.popleft()
        for i in range(4):
            nr = v[0] + dr[i]
            nc = v[1] + dc[i]
            if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 0:
                queue.append((nr, nc))
                graph[nr][nc] = 1


for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            cnt += 1
            start_idx = (i, j)
            bfs(graph, start_idx)

print(cnt)
