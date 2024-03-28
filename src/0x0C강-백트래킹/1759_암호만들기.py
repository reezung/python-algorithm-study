l, c = map(int, input().split())
a = input().split()
a.sort()

aeiou = {'a', 'e', 'i', 'o', 'u'}
s = []


def dfs(depth):
    if len(s) == l:
        if 1 <= len(aeiou & set(s)) <= l - 2:
            for i in s:
                print(i, end="")
            print()
        return
    for i in range(depth, c):
        s.append(a[i])
        dfs(i + 1)
        s.pop()


dfs(0)
