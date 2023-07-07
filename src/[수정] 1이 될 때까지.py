N, K = map(int, input().split())
cnt = 0
'''
1씩 빼는 과정을 한번에 처리하여
반복 횟수를 줄임
'''
while N > 1:
    if N // K < 1:
        cnt += N - 1
        break

    target = (N // K) * K
    cnt += N - target + 1
    N = N // K

print(cnt)
