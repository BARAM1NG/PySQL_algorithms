import sys

T = int(sys.stdin.readline())

for i in range(T):
  T_list = list(input())
  sum = 0
  
  for j in range(len(T_list)):
    if T_list[j] == '(':
      sum += 1
    else:
      sum -= 1
      
    if sum < 0:
      print('NO')
      break
    
  if sum > 0:
    print('NO')
  elif sum == 0:
    print('YES')