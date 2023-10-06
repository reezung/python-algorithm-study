'''
지훈이가 불이 타기 전에 탈출할 수 있는지의 여부,
그리고 얼마나 빨리 탈출할 수 있는지를 결정해야 한다.

미로의 가장자리에 접한 공간에서 탈출할 수 있다.
지훈이와 불은 벽이 있는 공간은 통과하지 못한다.


[edge case]
1. F가 0개이거나 F가 여러개
2. J가 이미 가장자리에 위치
'''
from collections import deque

r, c = map(int, input().split())
graph = [input() for _ in range(r)]
visited = [[0] * c for _ in range(r)]

F, J = [], []


def is_edge(i, j):
    return i == 0 or i == r - 1 or j == 0 or j == c - 1


def bfs():
    q = deque()
    # F -> J 순으로 bfs
    for f in F:
        q.append(f)
    q.append(J)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y, t = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if t == -1:
                    if visited[nx][ny] >= 0:    # 벽이 아니면 불이 번짐 (J가 이미 방문한 공간 포함)
                        q.append([nx, ny, -1])
                        visited[nx][ny] = -1
                else:
                    if visited[nx][ny] == 0:
                        q.append([nx, ny, t + 1])
                        visited[nx][ny] = 1

                        if is_edge(nx, ny):
                            print(t + 1)
                            exit(0)


for i in range(r):
    for j in range(c):
        if graph[i][j] != '.':
            if graph[i][j] == 'F':
                F.append([i, j, -1])
                visited[i][j] = -1  # F 번짐
            elif graph[i][j] == 'J':
                if is_edge(i, j):   # J가 이미 가장자리에 위치 => 1 출력 후 exit
                    print(1)
                    exit(0)
                J = [i, j, 1]
                visited[i][j] = 1   # J 방문
            else:
                visited[i][j] = -2  # 벽

bfs()
print("IMPOSSIBLE")
