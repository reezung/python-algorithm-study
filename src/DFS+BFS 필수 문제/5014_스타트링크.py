'''
잘 짠 것 같은데 통과되지 않을땐 변수 범위가 올바른지 확인하기,,
층수는 1 이상 f 이하임 (0 이상 아님)

bfs 턴수로 최단 경로를 구하는 문제
1697과 유사한 알고리즘
'''
from collections import deque


def bfs(start, end):
    q = deque([start])
    dist = [-1] * (f + 1)
    dist[start] = 0
    while q:
        x = q.popleft()
        if x == end:
            return dist[end]
        for nx in (x + u, x - d):
            if 0 < nx <= f and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)
    return 'use the stairs'


f, s, g, u, d = map(int, input().split())
print(bfs(s, g))
