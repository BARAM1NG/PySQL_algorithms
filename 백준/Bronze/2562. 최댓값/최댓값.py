N_list = []

for _ in range(9):
  A = int(input())
  N_list.append(A)


print(max(N_list))
print(N_list.index(max(N_list)) + 1)