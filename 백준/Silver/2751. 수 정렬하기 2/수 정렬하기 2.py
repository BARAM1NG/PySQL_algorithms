import sys
input = sys.stdin.readline

N = int(input())

N_list = [int(input()) for _ in range(N)]

N_list.sort()

for i in range(N):
  print(N_list[i])