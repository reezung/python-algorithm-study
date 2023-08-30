'''
이 문제의 권장 풀이는 BFS + 이진탐색임.
최소와 최대 중량을 정한 다음, mid를 통해 중간값을 계산해서 BFS를 통해 목적지까지 도달할 수 있을까 살펴보며
mid값을 이진탐색을 통해 조절해나간다.
'''
from collections import deque

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
low, high = 0, INF

for _ in range(m):
    a, b, e = map(int, input().split())
    graph[a].append((b, e))
    graph[b].append((a, e))

start, end = map(int, input().split())


def bfs(weight):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        if v == end:    # 목적지에 도달 가능
            return True
        for i, e in graph[v]:
            if not visited[i] and weight <= e:
                q.append(i)
                visited[i] = True
    return False    # 목적지에 도달 불가능


while low <= high:
    visited = [False] * (n + 1)
    mid = (low + high) // 2
    if bfs(mid): # 목적지까지 도달이 가능하다면 low를 올림
        low = mid + 1
    else:   # 목적지까지 불가능하다면 high를 내림
        high = mid - 1

print(high)
