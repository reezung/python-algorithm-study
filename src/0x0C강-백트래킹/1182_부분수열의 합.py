'''
중복없는 순열
'''
n, s = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0


def dfs(stack, idx):
    global cnt
    if stack and sum(stack) == s:
        cnt += 1
    for i in range(idx, n): #idx ~ n-1까지를 순회
        stack.append(a[i])
        dfs(stack, i + 1)
        stack.pop()


stack = []
dfs(stack, 0)
print(cnt)
