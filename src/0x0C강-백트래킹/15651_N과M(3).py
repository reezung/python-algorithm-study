n, m = map(int, input().split())
s = []


def dfs():
    if len(s) == m:
        for e in s:
            print(e, end=" ")
        print()
        return
    for i in range(1, n + 1):
        s.append(i)
        dfs()
        s.pop()


dfs()
