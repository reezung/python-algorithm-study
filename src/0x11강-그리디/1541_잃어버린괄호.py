'''
숫자 앞에 0이 오는 문자에 eval을 적용시키면 에러가 발생한다
'''
inp = input().split('-')
result = 0

for i in range(len(inp)):
    l = map(int, inp[i].split('+'))
    if i == 0:
        result += sum(l)
    else:
        result -= sum(l)

print(result)
