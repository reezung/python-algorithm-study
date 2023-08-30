inputs = list(input())
inputs.sort()
a = ""
n = 0
for i in inputs:
    if ord('0') <= ord(i) <= ord('9'):
        n += int(i)
    else:
        a += i

print(a + str(n))
