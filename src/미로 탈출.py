from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(graph, start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in range(4):
            nr = v[0] + dr[i]
            nc = v[1] + dc[i]
            if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] > 0:
                queue.append((nr, nc))
                if graph[nr][nc] == 1 and (nr, nc) != (0, 0):
                    graph[nr][nc] = graph[v[0]][v[1]] + 1
                if nr == N - 1 and nc == M - 1:
                    print(graph[nr][nc])
                    exit()


bfs(graph, (0, 0))
