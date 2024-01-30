N = int(input())

N_list = [input() for _ in range(N)]
N_list = set(N_list)
N_list = list(N_list)
N_list.sort()
N_list.sort(key = len)

for i in N_list:
  print(i)