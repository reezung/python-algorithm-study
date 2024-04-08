'''
사과를 먹였으면, apple 배열에서 해당 사과를 제거해주기!
'''
n = int(input())
k = int(input())
apple = [tuple(map(int, input().split())) for _ in range(k)]
l = int(input())
rotation = dict()
for _ in range(l):
    x, c = input().split()
    rotation[int(x)] = -1 if c == 'L' else 1

dx = [0, 1, 0, -1]  # +1 -> 오른쪽 90도, -1 -> 왼쪽 90도
dy = [1, 0, -1, 0]

t = 0
d = 0
snake = [(1, 1)]

while True:
    t += 1
    nx = snake[0][0] + dx[d]
    ny = snake[0][1] + dy[d]

    if (nx, ny) in snake or not (1 <= nx <= n and 1 <= ny <= n):
        print(t)
        break

    if (nx, ny) not in apple:
        snake.pop()
    else:
        apple.remove((nx, ny))

    if t in rotation:
        d = (d + rotation[t]) % 4

    snake.insert(0, (nx, ny))

