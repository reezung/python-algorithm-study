n, m = map(int, input().split())
a = list(map(int, input().split()))

s = []
ans = set()
def dfs():
    if len(s) == m:
        ans.add(tuple(s))
        return
    for i in a:
        s.append(i)
        dfs()
        s.pop()

dfs()
ans = list(ans)
ans.sort()
for i in ans:
    print(*i)