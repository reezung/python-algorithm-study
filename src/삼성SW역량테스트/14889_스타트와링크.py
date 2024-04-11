n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
stack = []
sub_stack = []
ans = int(1e9)


def calculate(t1):
    score1, score2 = [], []
    t2 = []
    for i in range(n):
        if i not in t1:
            t2.append(i)
    sub_dfs(0, t1, score1)
    sub_dfs(0, t2, score2)
    return abs(sum(score1) - sum(score2))


def sub_dfs(depth, t, score):
    if len(sub_stack) == 2:
        i, j = sub_stack
        score.append(s[i][j])
        score.append(s[j][i])
        return

    for i in range(depth, n // 2):
        sub_stack.append(t[i])
        sub_dfs(i + 1, t, score)
        sub_stack.pop()


def dfs(depth):
    global ans

    if stack and stack[0] != 0:
        return
    if len(stack) == n // 2:
        ans = min(ans, calculate(stack))
        return
    for i in range(depth, n):
        stack.append(i)
        dfs(i + 1)
        stack.pop()


dfs(0)
print(ans)
