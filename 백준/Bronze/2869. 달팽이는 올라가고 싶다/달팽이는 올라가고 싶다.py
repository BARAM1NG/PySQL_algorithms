A, B, V = map(int, input().split())

K = (V - B) % (A - B)

if K == 0:
    print((V - B) // (A - B))
else:
    print((V - B) // (A - B) + 1)
