s = input()
result = 0

x, y = s[1], s[0]
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]


def is_in_range(x, ascii_y):
    return 1 <= x <= 8 and ord('a') <= ascii_y <= ord('h')


for i in range(8):
    nx = int(x) + dx[i]
    ny = ord(y) + dy[i]
    if is_in_range(nx, ny):
        result += 1

print(result)
