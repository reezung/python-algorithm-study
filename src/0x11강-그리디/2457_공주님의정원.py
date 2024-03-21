'''
오늘 심을 수 있는 꽃의 조건: (sm, sd) <= latest_end < (em, ed)
이 조건을 만족하는 꽃들 중 가장 마지막에 지는 꽃을 찾아 심는다.
'''
n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
f.sort()

i = 0
result = 0
latest_end = (3, 1)

while i < n:
    sm, sd, em, ed = f[i]
    if (sm, sd) <= latest_end < (em, ed):
        max_end = (em, ed)
        while i < n-1:
            nsm, nsd, nem, ned = f[i+1]
            if latest_end < (nsm, nsd):
                break
            if max_end < (nem, ned):
                max_end = (nem, ned)
            i += 1
        # 오늘 심을 수 있는 꽃들 중에서, 가장 마지막에 지는 꽃을 심는다
        result += 1
        latest_end = max_end
        if (11, 30) < latest_end:
            print(result)
            exit(0)
    i += 1

print(0)
