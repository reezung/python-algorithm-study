N = int(input())
result = 0
num_in_three = 0    # 0~59 중에 3이 들어가는 숫자 개수
for i in range(60):
    if '3' in str(i):
        num_in_three += 1

for h in range(N + 1):
    if '3' in str(h):
        result += 60 * 60
    else:
        result += num_in_three * 60 + (60 - num_in_three) * num_in_three

print(result)
