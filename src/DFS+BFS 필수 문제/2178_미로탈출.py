'''
bfs는 한 레벨씩 탐색하므로, 최단거리는 bfs 탐색 턴 수.
노드의 초기값이 1임을 이용하면 현재 노드의 값(=진행된 bfs 탐색 턴 수)과 인접 노드의 값(=1)을 더하여 bfs 탐색 턴 수를 카운트할 수 있음.
노드를 처음 방문했을 때만 카운트해야하므로, graph[a][b] == 1일 때만 카운트한다.
'''
from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))


def bfs(sx, sy):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    print(graph[n-1][m-1])
    exit(0)


bfs(0, 0)
