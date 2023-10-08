'''
퀸들이 같은 열에 놓이거나 대각선에 위치하면 안됨
'''
n = int(input())
ans = 0
row = [0] * n


def is_promising(x):
    # x 이전의 모든 행에 대해 검사
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def n_queens(x):
    global ans, row
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            row[x] = i  # [x, i]에 퀸을 놓겠다
            if is_promising(x): # [x, i]에 퀸을 놓을 수 있으면
                n_queens(x + 1) # 그 다음행에 퀸을 놓으러


n_queens(0)
print(ans)
