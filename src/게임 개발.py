N, M = map(int, input().split())
x, y, d = map(int, input().split())
map_space = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx_left = [0, 1, 0, - 1]
dy_left = [-1, 0, 1, 0]
dx_back = [1, 0, -1, 0]
dy_back = [0, -1, 0, 1]

'''
방문 표시는 습관적으로
방문 리스트를 이용하자.
'''
visited[x][y] = 1
while True:
    for i in range(5):
        if i == 4:
            nx = x + dx_back[d]  # 바로 뒤쪽칸 이동 가능?
            ny = x + dy_back[d]
            if map_space[nx][ny] == 0:
                x, y = nx, ny
            else:
                print(sum(sum(r) for r in visited))
                exit()
        else:
            nx = x + dx_left[d]  # 바로 왼쪽칸 이동 가능?
            ny = y + dy_left[d]
            if map_space[nx][ny] == 0 and visited[nx][ny] == 0:
                x, y = nx, ny
                visited[nx][ny] = 1
                '''
                놀라운 사실
                -1 % 4 는 3이었다... .. .
                '''
                d = (d - 1) % 4  # 회전 방향은 왼쪽
                break
            else:
                d = (d - 1) % 4
