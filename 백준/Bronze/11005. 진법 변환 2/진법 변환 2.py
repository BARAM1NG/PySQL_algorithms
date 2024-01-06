N, B = map(int, input().split())
A = ''
arr = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')

while N:
    A += str(arr[N % B])
    N = N // B

print(A[::-1])