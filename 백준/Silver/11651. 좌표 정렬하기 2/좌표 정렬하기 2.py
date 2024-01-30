N = int(input())
N_list = []

for i in range(N):
  [x, y] = map(int, input().split())
  rev = [y, x]
  N_list.append(rev)
  
N_list.sort()

for i in range(N):
  print(N_list[i][1], N_list[i][0])