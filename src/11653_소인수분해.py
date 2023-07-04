N = int(input())
'''소인수분해 메서드'''
def factorization(n):
    k = 2
    while n != 1:
        if n % k == 0:
            print(k)
            n //= k
        else:
            k += 1

factorization(N)
