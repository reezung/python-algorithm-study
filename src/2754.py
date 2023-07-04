score = input()

if score == 'F':
    result = 0.0
else:
    result = 4.0 - (ord(score[0]) - ord('A'))
    if score[1] == '+':
        result += 0.3
    elif score[1] == '-':
        result -= 0.3

print(result)
