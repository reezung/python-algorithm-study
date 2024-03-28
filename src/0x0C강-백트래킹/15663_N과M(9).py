'''
중복체크 -> not in 연산자로 비교하면 오래걸림!!!

(cf) set을 활용해도 괜찮음
set의 원소로 넣으려면 리스트말고 튜플로 넣기
'''
n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = []
s = []


def dfs():
    if len(s) == m:
        ans.append([a[i] for i in s])
        return
    for idx in range(len(a)):
        if idx not in s:
            s.append(idx)
            dfs()
            s.pop()


dfs()
ans.sort()
# prev를 활용한 중복체크
prev = []
for curr in ans:
    if prev != curr:
        print(*curr)
        prev = curr
