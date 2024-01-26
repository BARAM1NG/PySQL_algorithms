N = int(input())
N_list = [int(input()) for _ in range(N)]

N_list.sort()

for i in N_list:
    print(i)