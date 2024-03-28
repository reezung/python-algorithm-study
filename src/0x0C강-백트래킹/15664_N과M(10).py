n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = []
ans = set()


def dfs(depth):
    if len(s) == m:
        ans.add(tuple([i for i in s]))
        return
    for i in range(depth, n):
        s.append(a[i])
        dfs(i + 1)
        s.pop()


dfs(0)
ans = list(ans)
ans.sort()
for i in ans:
    print(*i)
