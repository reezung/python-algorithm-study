'''
서로 같은 두 섬 사이에 여러 개의 다리가 있을 수 있음을 유의해야 함.
(즉, 노드 A와 B 사이에 여러 개의 간선이 있을 수 있음!)
그리고 메모리 제한이 128MB밖에 되지 않아서 플로이드 워셜 알고리즘을 사용할 수 없음.

1. (모든 노드에 대해) 두 노드 사이의 다리들 중 최대 중량을 버틸 수 있는 다리를 선택
2. 다익스트라 알고리즘을 응용하여,
        1) 경로 별로는 최대 중량을 선택.
        2) 경로 내부에서는 최소 중량을 선택.
   예를 들어 A<-2->B, A<-8->C<-10->B가 있다면
   경로 1에서는 2, 경로 2에서는 8을 선택하고
   경로 1과 경로 2에서는 경로 2(2 < 8)를 선택하여
   A - B의 옮길 수 있는 최대 중량은 8이 된다.
'''
import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
maxweight = [0] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start, end):
    q = []
    maxweight[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        w, curr_idx = heapq.heappop(q)  # 최대 힙 이용하여 큰 중량의 다리부터 선택
        weight = -1 * w
        if curr_idx == end:
            return weight
        if maxweight[curr_idx] > weight:  # 이미 최대 중량인 경우
            continue
        for i in graph[curr_idx]:
            if curr_idx == start:
                maxweight[i[0]] = i[1]
                heapq.heappush(q, (-1 * maxweight[i[0]], i[0]))
            elif maxweight[i[0]] < min(weight, i[1]):   # 경로 별로는 최대 중량을 선택 max(maxweight[i[0]], min(weight, i[1]))
                maxweight[i[0]] = min(weight, i[1])     # 경로 내부에서는 최소 중량을 선택 min(weight, i[1])
                heapq.heappush(q, (-1 * maxweight[i[0]], i[0]))


ns, ne = map(int, input().split())
print(dijkstra(ns, ne))
