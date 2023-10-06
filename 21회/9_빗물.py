'''
left_max, right_max를
max 함수를 이용하여 쉽게 계산
'''
h, w = map(int, input().split())
heights = list(map(int, input().split()))

ans = 0
for i in range(1, w-1):
    left_max = max(heights[:i])
    right_max = max(heights[i+1:])

    compare = min(left_max, right_max)

    if heights[i] < compare:
        ans += compare-heights[i]

print(ans)