N = int(input())
is_cute = 0
for _ in range(N):
    is_cute += int(input())

if is_cute > N//2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')