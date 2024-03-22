'''
A의 원소는 모두 다름
수열이 오름차순이도록
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
        if not s or a > s[-1]:
            s.append(a)
            dfs()
            s.pop()


dfs()
