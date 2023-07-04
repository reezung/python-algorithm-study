points = [tuple(map(int, input().split())) for _ in range(3)]
x = [p[0] for p in points]
y = [p[1] for p in points]


def find_point(l):
    if l[0] == l[1]:
        return l[2]
    elif l[0] == l[2]:
        return l[1]
    else:
        return l[0]


print(find_point(x), find_point(y))
