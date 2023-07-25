n, m = map(int, input().split())
tteok_list = list(map(int, input().split()))
max_len = max(tteok_list)
curr = -1


def calculate_length(target):
    total_len = 0
    for t in tteok_list:
        if t > target:
            total_len += t - target
    return total_len


def binary_search(target, start, end):
    global curr

    while start <= end:
        mid = (start + end) // 2
        mid_len = calculate_length(mid)
        if mid_len == target:
            curr = mid
            break
        elif mid_len > target:
            curr = mid
            start = mid + 1
        else:
            end = mid - 1
        # print(curr)
    return curr


print(binary_search(m, 0, max_len))
