import heapq

INF = int(1e9)

n, m = map(int, input().split())
s = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
visited = [0] * (n + 1)

for _ in range(m):
    i, j, e = map(int, input().split())
    graph[i].append((j, e))


def dijkstra(start):
    global graph, distance
    q = []
    heapq.heappush(q, (0, start))   # 거리 순으로 힙정렬
    distance[start] = 0
    while q:
        dist, curr_idx = heapq.heappop(q)
        if distance[curr_idx] < dist:   # 큐에 넣은 이후에 curr_idx의 최단경로가 갱신된 경우
            continue
        for i in graph[curr_idx]:
            if distance[i[0]] > dist + i[1]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (distance[i[0]], i[0]))   # 최단경로가 갱신된 경우, 우선순위 큐에 삽입


def print_distance():
    for i in distance[1:]:
        if i == INF:
            print("INFINITY")
        else:
            print(i)


dijkstra(s)
print_distance()
