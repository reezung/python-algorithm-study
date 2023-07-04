T = int(input())
ta = 300
tb = 60
tc = 10

if T % 10 != 0:
    print(-1)
else:
    '''
    그리디 알고리즘이 가능한 이유:
    ta, tb, tc의 최대공약수가 ta, tb, tc 중에 있음
    따라서 그리디하게 선택한 다음, 남은 시간을 최대공약수 tc로 채우면 최소 조작수가 됨
    '''
    A = B = C = 0
    A = T // ta
    B = (T % ta) // tb
    C = (T % ta) % tb // tc
    print(A, B, C)
