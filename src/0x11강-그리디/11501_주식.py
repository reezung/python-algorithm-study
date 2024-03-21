'''
앞에서부터 순회하면
중간에 나온 최댓값이 뒤에 나올 최댓값보다 큰지 작은지 알 수 없어 곧바로 그리디 적용 불가능 => 비교하기 위한 시간 소요

***
하지만 뒤에서부터 순회하면
무조건 지금 나온 최댓값을 적용하면 되므로, 그리디 알고리즘 적용 가능
'''
t = int(input())
for _ in range(t):
    n = int(input())
    stocks = list(map(int, input().split()))
    money = 0
    max_stock = 0
    for i in range(n-1, -1, -1):
        if stocks[i] > max_stock:
            max_stock = stocks[i]
        else:
            money += max_stock - stocks[i]
    print(money)