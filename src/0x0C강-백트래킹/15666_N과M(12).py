'''
depth를 설정하는 로직에서,
중복 선택 허용이므로, dfs(i+1)이 아닌, dfs(i)를 넘겨준다
'''
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

s = []
ans = set()


def dfs(depth):
    if len(s) == m:
        ans.add(tuple(s))
        return
    for i in range(depth, n):
        s.append(a[i])
        dfs(i)
        s.pop()


dfs(0)
ans = list(ans)
ans.sort()
for i in ans:
    print(*i)
