N = int(input())
plan = input().split()
curr = [1, 1]


def move(type):
    global curr
    if type == "R":
        if curr[1] != N:
            curr[1] += 1
    elif type == "L":
        if curr[1] != 1:
            curr[1] -= 1
    elif type == "U":
        if curr[0] != 1:
            curr[0] -= 1
    else:
        if curr[0] != N:
            curr[0] += 1


for d in plan:
    move(d)

for res in curr:
    print(res, end=" ")
