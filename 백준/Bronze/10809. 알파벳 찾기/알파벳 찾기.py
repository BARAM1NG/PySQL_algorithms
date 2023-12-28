S = input()
C = 'abcdefghijklmnopqrstuvwxyz'

for i in C:
  if i in S:
    print(S.index(i), end = ' ')
  else:
    print(-1, end = ' ')
