N = int(input())
num_list = [int(input()) for _ in range(N)]

num_list.sort(reverse=True)
print(num_list, end=" ")
