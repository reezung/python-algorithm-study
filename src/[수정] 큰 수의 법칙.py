N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort(reverse=True)

first = num_list[0]
second = num_list[1]
'''
반복되는 수열임을 이용하여
더하는 횟수를 구한 다음, 한번에 더해서 결과를 구함
'''
first_count = (M // (K + 1)) * K + M % (K + 1)
second_count = M // (K + 1)

result = first * first_count + second * second_count
print(result)
