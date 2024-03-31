import sys

N = int(sys.stdin.readline())
Deque = []

for _ in range(N):
  a = sys.stdin.readline().split()
  if a[0] == 'push_front':
    Deque.insert(0, a[1])
  elif a[0] == 'push_back':
    Deque.append(a[1])
  elif a[0] == 'pop_front':
    if len(Deque) == 0:
      print(-1)
    else:
      print(Deque.pop(0))
  elif a[0] == 'pop_back':
    if len(Deque) == 0:
      print(-1)
    else:
      print(Deque.pop())
  elif a[0] == 'size':
    print(len(Deque))
  elif a[0] == 'empty':
    if len(Deque) == 0:
      print(1)
    else:
      print(0)
  elif a[0] == 'front':
    if len(Deque) == 0:
      print(-1)
    else:
      print(Deque[0])
  else:
    if len(Deque) == 0:
      print(-1)
    else:
      print(Deque[-1])