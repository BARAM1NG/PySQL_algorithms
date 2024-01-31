N = int(input())
N_list = []

for i in range(N):
  age, name = input().split()
  age = int(age)
  N_list.append((age, name))

N_list.sort(key = lambda x : x[0])

for i in N_list:
  print(i[0], i[1])