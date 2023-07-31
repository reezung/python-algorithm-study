n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


def find_team(parent, a):
    if parent[a] != a:
        parent[a] = find_team(parent, parent[a])
    return parent[a]


def union_team(parent, a, b):
    a = find_team(parent, a)
    b = find_team(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    type, s1, s2 = map(int, input().split())
    if type == 0:
        union_team(parent, s1, s2)
    else:
        if find_team(parent, s1) == find_team(parent, s2):
            print("YES")
        else:
            print("NO")
