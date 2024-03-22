'''
중복없는 조합
'''
n, m = map(int, input().split())


def dfs(s):
    if len(s) == m:
        for e in s:
            print(e, end=" ")
        print()
        return
    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs(s)
            s.pop()


s = []
dfs(s)