n = int(input())
parts_list = list(map(int, input().split()))
m = int(input())
wants_list = list(map(int, input().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 'yes'
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 'no'


for i in wants_list:
    print(binary_search(parts_list, i, 0, n - 1), end=" ")
