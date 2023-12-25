N, M = map(int, input().split())
N_list = []

for i in range(1, N+1):
  N_list.append(i)

for _ in range(M):
  # i번과 j번 바구니의 공을 바꾼다.
  i, j = map(int, input().split())
  temp = N_list[i - 1]
  N_list[i - 1] = N_list[j - 1]
  N_list[j-1] = temp

for i in range(N):
  print(N_list[i], end = ' ')