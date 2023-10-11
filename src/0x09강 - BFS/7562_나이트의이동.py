from collections import deque

t = int(input())


def bfs(l, s, d, visited):
    q = deque([s])
    visited[s[0]][s[1]] = 1

    dx = [1, 1, 2, 2, -1, -1, -2, -2]
    dy = [2, -2, 1, -1, 2, -2, 1, -1]

    while q:
        x, y = q.popleft()
        if (x, y) == d:
            return visited[x][y]-1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


for _ in range(t):
    l = int(input())
    s = tuple(map(int, input().split()))
    d = tuple(map(int, input().split()))

    visited = [[0] * l for _ in range(l)]
    print(bfs(l, s, d, visited))
