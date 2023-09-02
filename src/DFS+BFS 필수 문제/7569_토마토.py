from collections import deque

m, n, h = map(int, input().split())
graph = []
queue = deque()
day = 1 # 걸린 일수
cnt = 0  # 남아 있는 익지 않은 토마토 개수

# 왼, 오, 위, 아래, 앞, 뒤
dx = [0, 0, 0, 0, -1, 1]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 1, -1, 0, 0]


def is_in_range(x, y, z):
    return 0 <= x < n and 0 <= y < m and 0 <= z < h


def bfs():
    global graph, cnt, day, queue
    while queue:
        x, y, z = queue.popleft()
        if x == -1 and y == -1 and z == -1:
            if queue:
                day += 1
                queue.append((-1, -1, -1))
                continue
            else:
                # 익지 않은 토마토가 남은 채로 큐가 빈 경우
                print(-1)
                exit(0)
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if is_in_range(nx, ny, nz) and graph[nz][nx][ny] == 0:
                cnt -= 1
                graph[nz][nx][ny] = 1
                queue.append((nx, ny, nz))  # 새로 익은 토마토의 위치를 큐에 삽입
                if cnt == 0:
                    print(day)
                    exit(0)


for i in range(h):
    temp = []
    for j in range(n):
        inp = list(map(int, input().split()))
        cnt += inp.count(0)
        temp.append(inp)
        for k in range(m):
            if inp[k] == 1:
                queue.append((j, k, i)) # 익은 토마토의 위치를 큐에 삽입
    graph.append(temp)
queue.append((-1, -1, -1))  # (-1,-1,-1) : 1회를 모두 탐색했음을 알려줌

if cnt == 0:
    print(0)
else:
    bfs()
