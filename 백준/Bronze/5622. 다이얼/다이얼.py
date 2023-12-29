dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
ret = 0

S = input()

for i in range(len(S)):
  for j in dial:
    if S[i] in j:
      ret += dial.index(j)+3

print(ret)