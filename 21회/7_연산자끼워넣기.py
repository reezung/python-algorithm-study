'''
* 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다.
* 나눗셈은 정수 나눗셈으로 몫만 취한다
* 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다
'''
n = int(input())
a = list(map(int, input().split()))
cal = list(map(int, input().split()))  # +, -, *, //
ans = []


def calculate(curr, x, i):
    symbols = ['+', '-', '*', '//']
    if curr < 0 and i == 3:
        return -((-curr) // x)
    else:
        return int(eval(str(curr) + symbols[i] + str(x)))


# 연산자 우선순위 무시 -> 현재까지의 계산 결과를 curr에 저장
def dfs(a, cal, curr):
    if not a:
        ans.append(curr)
        return

    x = a[0]
    for i in range(4):
        if cal[i] > 0:
            # dfs 과정에서 a, cal, curr 값이 바뀌지 않도록 주의
            ncal = [c for c in cal]
            ncal[i] -= 1
            ncurr = calculate(curr, x, i)

            dfs(a[1:], ncal, ncurr)


dfs(a[1:], cal, a[0])

print(max(ans))
print(min(ans))
