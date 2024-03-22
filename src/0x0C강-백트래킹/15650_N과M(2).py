n, m = map(int, input().split())
s = []


def dfs(start):
    if len(s) == m:
        for e in s:
            print(e, end=" ")
        print()
        return
    for i in range(start, n+1):
        s.append(i)
        dfs(i+1)
        s.pop()


dfs(1)
