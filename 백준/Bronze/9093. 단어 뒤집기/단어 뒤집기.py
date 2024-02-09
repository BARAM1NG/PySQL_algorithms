T = int(input())

sequence = list([input().split() for _ in range(T)])

for i in range(len(sequence)):
  for j in sequence[i]:
    print(j[::-1], end = ' ')
  print("")