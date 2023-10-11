from collections import deque

n = int(input())
k = int(input())
apples = [tuple(map(int, input().split())) for _ in range(k)]
l = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
di = dict()

for i in range(l):
    x, c = input().split()
    if c == 'D':
        di[int(x)] = 1  # 오른쪽 회전(D): (i+1)%4
    else:
        di[int(x)] = -1 # 왼쪽 회전(L): (i-1)%4


def move():
    q = deque([(1, 1)]) # 뱀이 위치한 좌표
    t = 0
    i = 0
    while True:
        x, y = q[-1]

        nx = x + dx[i]
        ny = y + dy[i]
        t += 1

        if 0 < nx <= n and 0 < ny <= n:
            if (nx, ny) in q:
                return t

            if (nx, ny) not in apples:
                q.popleft() # 꼬리 삭제
            else:
                apples.remove((nx, ny)) # 사과 먹음

            q.append((nx, ny))
        else:
            return t

        i = (i + di[t]) % 4 if t in di.keys() else i


print(move())
