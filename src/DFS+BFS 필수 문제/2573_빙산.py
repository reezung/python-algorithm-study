from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
year = 0


def bfs(x, y):
    q = deque([(x, y)])
    q_zero = []
    visited[x][y] = True
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    cnt += 1
                elif graph[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True  # 이걸 안해주면 시간초과
                    q.append((nx, ny))
        if graph[x][y] > cnt:
            graph[x][y] -= cnt
        else:
            q_zero.append((x, y))

    while q_zero:
        x, y = q_zero.pop()
        graph[x][y] = 0


while True:
    result = 0
    visited = [[False]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if graph[x][y] > 0 and not visited[x][y]:
                result += 1
                if result == 2:
                    print(year)
                    exit(0)
                else:
                    bfs(x, y)
    year += 1
    if sum(sum(g) for g in graph) == 0:
        print(0)
        exit(0)