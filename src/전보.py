import heapq

INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b, e = map(int, input().split())
    graph[a].append((b, e))


def dijkstra(start):
    global distance, graph
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, curr = heapq.heappop(q)
        if distance[curr] < dist:
            continue
        for i in graph[curr]:
            if distance[i[0]] > i[1] + dist:
                distance[i[0]] = i[1] + dist
                heapq.heappush(q, (distance[i[0]], i[0]))


def print_result():
    cnt = 0
    time = 0
    for i in distance[1:]:
        if i != INF:
            cnt += 1
            time = max(time, i)
    print(cnt-1, time)


dijkstra(c)
print_result()
