X = int(input())
N = int(input())

# 물건 가격 총합
C = 0

for _ in range(N):
  A, B = map(int, input().split())
  C += A * B

if X == C:
  print('Yes')
else:
  print('No')