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
graph = [list(input()) for _ in range(r)]


def bfs():
    global j
    q = deque()
    for x in range(r):
        for y in range(c):
            if graph[x][y] == 'J':
                j = (x, y, 1)
            elif graph[x][y] == 'F': # 불이 여러개일 수 있음
                q.append((x, y, -1))
    q.append(j) # F -> J 순으로 bfs
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y, cnt = q.popleft()
        if cnt != -1 and (x in [0, r - 1] or y in [0, c - 1]):
            print(cnt)
            exit(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if cnt == -1 and graph[nx][ny] not in ['#', 'F']:
                    q.append((nx, ny, -1))
                    graph[nx][ny] = 'F'
                elif cnt > -1 and graph[nx][ny] == '.':
                    q.append((nx, ny, cnt + 1))
                    graph[nx][ny] = 'J'


bfs()
print("IMPOSSIBLE")
