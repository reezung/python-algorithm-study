n = int(input())
units = list(map(int, input().split()))
units.sort()
'''
target >= unit이면 
target을 만들 수 있는 이유:

target = (target-unit) + unit
이때, 1 <= target-unit <= target-1 이므로
(target-unit)을 만들 수 있음.

따라서 target >= unit이면 target을 만들 수 있음
'''
target = 1
for unit in units:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < unit:
        break
    target += unit

print(target)

