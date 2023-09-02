'''
영역 개수를 세는 문제는 dfs와 bfs 모두로 풀이할 수 있음
dfs는 재귀 횟수 제한에 걸릴 수 있으므로, bfs로 풀이하는게 더 안전함
'''
from collections import deque


def bfs(graph, x, y):
    q = deque([(x, y)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
MAX = max([max(g) for g in graph])
result = 0
for h in range(MAX + 1):
    temp = [[1 if j > h else 0 for j in i] for i in graph]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if temp[x][y] == 1:
                cnt += 1
                temp[x][y] = 0
                bfs(temp, x, y)
    result = max(cnt, result)
print(result)
