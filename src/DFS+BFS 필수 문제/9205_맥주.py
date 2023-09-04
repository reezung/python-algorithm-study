'''
1. 집-목적지 사이의 거리가 1000m 이하이면 happy
2. 집-편의점 사이의 거리가 1000m 이하이면 편의점으로 이동
    (= q에 편의점 위치 삽입 후 편의점 위치 방문체크)
'''
from collections import deque


def bfs(start, goal):
    q = deque([start])
    gx, gy = goal
    beer = 20
    visited = [False] * n
    while q:
        x, y = q.popleft()
        if abs(x - gx) + abs(y - gy) <= 50 * beer:
            print('happy')
            return
        for i in range(n):
            mx, my = market[i]
            if abs(x - mx) + abs(y - my) <= 50 * beer and not visited[i]:
                q.append((mx, my))
                visited[i] = True
    print('sad')
    return


t = int(input())
for _ in range(t):
    n = int(input())
    start = tuple(map(int, input().split()))
    market = [tuple(map(int, input().split())) for _ in range(n)]
    goal = tuple(map(int, input().split()))

    bfs(start, goal)
