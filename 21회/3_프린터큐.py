t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    xCnt, pCnt = 0, 0

    while True:
        x = q[xCnt % n]

        if x == -1:
            continue

        if max(q) == x:
            pCnt += 1   # 프린트 횟수 += 1
            q[xCnt % n] = -1    # 방문 체크
            if xCnt % n == m:
                print(pCnt)
                break

        xCnt += 1
