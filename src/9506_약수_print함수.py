'''
약수 구하는 메소드
약수는 1 ~ n//2 사이에 존재
'''
def divisor(n):
    div = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            div.append(i)
    return div


while True:
    n = int(input())
    if n == -1:
        break
    elif n == sum(divisor(n)):
        print(f"{n}", end=" = ")    # print 함수의 end
        print(*divisor(n), sep=" + ")   # print 함수의 sep. *를 붙이면 여러개의 인수가 들어간다는 의미
    else:
        print(f"{n} is NOT perfect.")
