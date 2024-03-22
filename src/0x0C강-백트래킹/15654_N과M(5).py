'''
A 원소들이 모두 다름
'''
n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
s = []


def dfs():
    if len(s) == m:
        for e in s:
            print(e, end=" ")
        print()
        return
    for a in A:
        if a not in s:
            s.append(a)
            dfs()
            s.pop()


dfs()
