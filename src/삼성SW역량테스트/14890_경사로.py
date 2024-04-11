n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
board_v = [[board[j][i] for j in range(n)] for i in range(n)]
board += board_v

cnt = 0
for b in board:
    visited = [0]*n
    prev = b[0]
    cnt += 1
    for i in range(1, n):
        if b[i] == prev:
            continue
        elif b[i] == prev + 1:
            if i - l >= 0 and b[i-l: i] == [prev]*l and visited[i-l: i] == [0]*l:
                prev = b[i]
                visited[i-l: i] = [1]*l
                continue
        elif b[i] == prev - 1:
            if i + l <= n and b[i: i+l] == [prev-1]*l and visited[i: i+l] == [0]*l:
                prev = b[i]
                visited[i: i+l] = [1]*l
                continue

        cnt -= 1
        break

print(cnt)
