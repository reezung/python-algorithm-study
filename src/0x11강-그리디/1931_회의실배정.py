n = int(input())
l = [tuple(map(int, input().split())) for _ in range(n)]
"""
졍렬을 
(1) 끝나는 시간의 오름차순 뿐만 아니라
(2) 시작하는 시간의 오름차순으로도 해줘야함!

2
2 2
1 2
에서 (1,2), (2,2)로 2회 가능하지만
(2,2), (1,2) 순으로 정렬될 경우 1회라는 답이 나오기 때문

=> 그리디에선 정렬 순서가 매우 중요!
"""
l.sort(key=lambda x: (x[1], x[0]))

result = 0
latest_end = 0

for li in l:
    if li[0] >= latest_end:
        result += 1
        latest_end = li[1]

print(result)
