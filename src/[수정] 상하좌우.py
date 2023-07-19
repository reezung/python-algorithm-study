N = int(input())
plan = input().split()
x, y = 1, 1
'''
이동 문제에서 dx, dy를 정의하여
반복문으로 nx, ny를 구함
'''
types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def move(type):
    global x, y
    for i in range(len(types)):
        if types[i] == type:
            nx = x + dx[i]
            ny = y + dy[i]
            if is_in_range(nx) and is_in_range(ny):
                x, y = nx, ny
            break


def is_in_range(n):
    return 1 <= n <= N


for d in plan:
    move(d)

print(x, y)
