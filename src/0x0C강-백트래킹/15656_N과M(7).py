n, m = map(int, input().split())
a = list(map(int, input().split()))

s = []


def dfs():
    if len(s) == m:
        for i in s:
            print(i, end=" ")
        print()
        return
    for i in a:
        s.append(i)
        dfs()
        s.pop()

a.sort()
dfs()
