'''
그리디
1. students를 end time으로 sort
2. students 순회하며 순서대로 studnets_start - 슬롯_end의 값이 더 작은 슬롯에 배치
'''
n = int(input())
s = list(map(int, input().split()))
e = list(map(int, input().split()))

students = [(e[i], s[i]) for i in range(n)]
students.sort()

e1, e2, cnt = 0, 0, 0

for std in students:
    te, ts = std
    if e1 > ts and e2 > ts:
        continue

    cnt += 1
    if e1 <= ts and e2 <= ts:
        if ts - e1 <= ts - e2:
            e1 = te
        else:
            e2 = te
    elif e1 <= ts:
        e1 = te
    else:
        e2 = te

print(cnt)