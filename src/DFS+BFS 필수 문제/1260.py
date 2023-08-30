'''
간선이 양방향이면 graph[a].append(b)와 graph[b].append(a)를 모두 해주어야 함.

'''
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()


def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    print()
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


dfs(v)
bfs(v)
