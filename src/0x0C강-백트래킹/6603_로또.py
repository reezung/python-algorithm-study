stack = []


def dfs(k, s, depth):
    if len(stack) == 6:
        print(*stack)
        return
    for i in range(depth, k):
        stack.append(s[i])
        dfs(k, s, i + 1)
        stack.pop()


while True:
    inp = list(map(int, input().split()))
    if inp[0] == 0:
        break
    k = inp[0]
    s = inp[1:]
    dfs(k, s, 0)
    print()