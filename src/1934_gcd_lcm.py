T = int(input())
'''
유클리드 호제법을 이용한 최대공약수 메소드
gcd(a, b) = gcd(b, a%b) 
if a%b == 0 -> gcd는 b
'''
def gcd(a, b):
    while a % b != 0:
        temp = b
        b = a % b
        a = temp
    return b
'''
최소공배수 메소드
lcm은 (a * b) // gcd(a, b)
'''
def lcm(a, b):
    return a * b // gcd(a, b)

for _ in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))