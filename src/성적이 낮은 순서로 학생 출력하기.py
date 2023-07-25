N = int(input())
A = [input().split() for _ in range(N)]


def score(info):
    return int(info[1])


A.sort(key=score)
for i in A:
    print(i[0], end=" ")
