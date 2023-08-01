s = list(map(int, input()))
result = s[0]
'''
0뿐만 아니라 1도 더하기를 수행한 결과값이 더 크다
'''
for i in range(1, len(s)):
    if s[i] <= 1 or result <= 1:
        result += s[i]
    else:
        result *= s[i]

print(result)
