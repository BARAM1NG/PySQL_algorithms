N = int(input())
X_list = []
Y_list = []

for _ in range(N):
    a, b = map(int,input().split())
    X_list.append(a)
    Y_list.append(b)

if N < 2:
    print(0)
else:
    print((max(X_list)-min(X_list)) * (max(Y_list) - min(Y_list)))
