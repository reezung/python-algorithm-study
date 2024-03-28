n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

s = []
def dfs(depth):
    if len(s) == m:
        for i in s:
            print(i, end=" ")
        print()
        return
    for i in range(depth, len(a)):
        s.append(a[i])
        dfs(i)
        s.pop()

dfs(0)