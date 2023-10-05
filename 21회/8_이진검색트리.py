import sys

sys.setrecursionlimit(10 ** 6)

tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break


def binary_search(left, right, tree, result):
    if left > right:
        return

    root = tree[left]
    tmp = left + 1
    for i in range(left + 1, right + 1):
        if tree[i] > root:
            tmp = i
            break

    binary_search(left + 1, tmp - 1, tree, result)
    binary_search(tmp, right, tree, result)

    result.append(root)


result = []
binary_search(0, len(tree) - 1, tree, result)

for r in result:
    print(r)
