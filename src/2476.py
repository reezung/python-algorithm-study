N = int(input())
m = 0 # max 상금 저장


def reward(d):
    d_del = set(d)  # 중복 제거
    if len(d_del) == 1:
        return 10000 + d[0] * 1000
    elif len(d_del) == 2:
        same = (lambda k: k[0] if k[0] == k[1] or k[0] == k[2] else k[1])(d)
        return 1000 + same * 100
    else:
        return max(d) * 100


for _ in range(N):
    dice = list(map(int, input().split()))
    if reward(dice) > m:
        m = reward(dice)

print(m)