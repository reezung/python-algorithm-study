n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []


def dfs(v, cnt):
    cnt += 1
    visited[v] = True
    if v == p2:
        result.append(cnt)
    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt)


cnt = 0
dfs(p1, cnt)
if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)
