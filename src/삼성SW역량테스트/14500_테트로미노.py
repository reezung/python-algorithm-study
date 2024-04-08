n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s = []
_ans = 0
_sum = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global _ans, _sum
    if len(s) == 4:
        _ans = max(_ans, _sum)
        return

    if len(s) == 3:
        if s[0][0] == s[1][0] == s[2][0]:
            for i in [-1, 1]:
                nx = s[1][0] + i
                ny = s[1][1]
                if 0 <= nx < n and 0 <= ny < m:
                    s.append((nx, ny))
                    _sum += board[nx][ny]
                    dfs(nx, ny)
                    s.pop()
                    _sum -= board[nx][ny]
        elif s[0][1] == s[1][1] == s[2][1]:
            for i in [-1, 1]:
                nx = s[1][0]
                ny = s[1][1] + i
                if 0 <= nx < n and 0 <= ny < m:
                    s.append((nx, ny))
                    _sum += board[nx][ny]
                    dfs(nx, ny)
                    s.pop()
                    _sum -= board[nx][ny]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in s:
            s.append((nx, ny))
            _sum += board[nx][ny]
            dfs(nx, ny)
            s.pop()
            _sum -= board[nx][ny]


for x in range(n):
    for y in range(m):
        s.append((x, y))
        _sum += board[x][y]
        dfs(x, y)
        s.pop()
        _sum -= board[x][y]

print(_ans)
