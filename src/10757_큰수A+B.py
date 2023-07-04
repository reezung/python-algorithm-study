A, B = input().split()
A = A[::-1]
B = B[::-1]
if len(A) > len(B):
    B += "0" * (len(A) - len(B))
elif len(A) < len(B):
    A += "0" * (len(B) - len(A))

result = ""
flag = 0
for i in range(len(A)):
    result += str((int(A[i]) + int(B[i]) + flag) % 10)
    flag = (int(A[i]) + int(B[i]) + flag) // 10
if flag > 0:
    result += str(flag)
print(result[::-1])
