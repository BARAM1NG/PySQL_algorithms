N = int(input())
A = 0

for i in range(N+1):
  if A % 4 == 0 and A != 0:
    print('long', end=' ')
  A += 1
print('int', end='')