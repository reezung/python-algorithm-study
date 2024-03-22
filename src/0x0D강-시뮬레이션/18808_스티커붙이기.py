import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]
stickers = []

for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(sticker)


def rotate(idx):
    sticker = stickers[idx]
    temp = []
    for c in range(len(sticker[0])):
        row = []
        for r in range(len(sticker) - 1, -1, -1):
            row.append(sticker[r][c])
        temp.append(row)
    stickers[idx] = temp


def attach(x, y, sticker):
    for dx in range(len(sticker)):
        for dy in range(len(sticker[0])):
            nx = x + dx
            ny = y + dy
            if sticker[dx][dy] == 1:
                board[nx][ny] = 1


def is_available(x, y, sticker):
    for dx in range(len(sticker)):
        for dy in range(len(sticker[0])):
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < n and 0 <= ny < m):
                return False
            if sticker[dx][dy] + board[nx][ny] > 1:
                return False
    attach(x, y, sticker)
    return True


def check_sticker(idx):
    for _ in range(4):
        for x in range(n):
            for y in range(m):
                if is_available(x, y, stickers[idx]):
                    return # 붙임
        rotate(idx)


for idx in range(k):
    check_sticker(idx)

print(sum([sum(r) for r in board]))
