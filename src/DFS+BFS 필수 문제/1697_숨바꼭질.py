'''
그리디 알고리즘으로 풀면 안됨.
dp 알고리즘으로도 풀 수 없음.
=> 앞으로만 움직일 수 있는게 아니고, 뒤로도 움직일 수 있기 때문.
   알고리즘이 진행되는 과정에서 미리 계산해놓은 부분문제의 값이 자꾸 업데이트되므로, 큰 문제의 값도 업데이트시켜주어야 함.

따라서 거리가 업데이트 된 위치를 큐에 삽입하여, 나머지 값들도 다시 업데이트해주어야 함
'''
from collections import deque

INF = int(1e9)
MAX = 10 ** 5
n, k = map(int, input().split())
dist = [INF] * (MAX + 1)
dist[n] = 0


def bfs(start):
    q = deque([start])
    while q:
        x = q.popleft()
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= MAX and dist[i] > dist[x] + 1:
                dist[i] = dist[x] + 1
                q.append(i)


bfs(n)
print(dist[k])
