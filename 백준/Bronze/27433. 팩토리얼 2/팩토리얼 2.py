N = int(input())

N_factorial_list = [i for i in range(1, N+1)]

N_factorial = 1

for i in N_factorial_list:
  N_factorial *= i
  
print(N_factorial)