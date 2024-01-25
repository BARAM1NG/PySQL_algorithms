N = int(input())

a = 1

for i in range(N):
    a += i * 6
    if N <= a:
        print(i + 1)
        break