M = int(input())
N = int(input())
A = []

for i in range(M, N+1):
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                A.append(j)
            
            break

if len(A) == 0:
    print(-1)
else:
    print(sum(A))
    print(min(A))
