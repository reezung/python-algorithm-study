n, m = map(int, input().split())
s = []  # dfs 외부에 선언


def dfs():
    # 종료조건
    if len(s) == m:
        for i in s:
            print(i, end=" ")
        print()
        return
    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()  # 백트래킹


dfs()
