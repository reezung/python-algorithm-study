n = int(input())
a = list(map(int, input().split()))
operators_state = list(map(int, input().split()))
operators = ['+', '-', '*', '//']
s = []
res = []


def calculate(o):
    ans = a[0]
    for i in range(n - 1):
        sign = 1
        if ans < 0 and o[i] == '//':
            sign = -1
        ans = eval(str(ans*sign) + o[i] + str(a[i + 1]))
        ans *= sign
    return ans


def dfs():
    if len(s) == n - 1:
        x = [i for i in s]
        res.append(calculate(x))
        return
    for i in range(4):
        if operators_state[i] > 0:
            s.append(operators[i])
            operators_state[i] -= 1
            dfs()
            s.pop()
            operators_state[i] += 1


dfs()
print(max(res))
print(min(res))
