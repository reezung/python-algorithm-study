INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

x, k = map(int, input().split())


def floyd_warshall(graph):
    for k in range(1, n + 1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


floyd_warshall(graph)
dist = graph[1][k] + graph[k][x]
print(dist if dist < INF else -1)
