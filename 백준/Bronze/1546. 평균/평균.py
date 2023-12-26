N = int(input())
N_list = list(map(int, input().split()))
M = max(N_list)

for i in range(N):
  N_list[i] = N_list[i]/M*100

print(sum(N_list)/N)