score = [int(input()) for _ in range(5)]
sum = 0
for s in score:
    # lambda 함수에서 if 문을 쓸 때
    sum += (lambda a: 40 if a<40 else a)(s)
print(sum//5)