import sys
input = sys.stdin.readline

N = input()
N_list = []

for i in range(len(N)):
  N_list.append(N[i])

N_list.sort(reverse = True)

for i in range(len(N)):
  print(N_list[i], end = "")