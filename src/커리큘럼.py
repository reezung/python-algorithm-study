from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
costs = [0] * (n + 1)

for i in range(1, n + 1):
    inputs = list(map(int, input().split()))
    costs[i] = inputs[0]
    graph[i] = inputs[1:-1]
    indegree[i] = len(graph[i])


def topology_sort():
    result = [c for c in costs]
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in range(1, n + 1):
            if now in graph[i]:
                result[i] = max(result[i], result[now] + costs[i])
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    for r in result[1:]:
        print(r)


topology_sort()
