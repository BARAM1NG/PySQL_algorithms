T = int(input())

a = 25
b = 10
c = 5
d = 1

for _ in range(T):
    A = int(input())
    A_count = A // a
    B_count = (A - A_count * a) // b
    C_count = (A - A_count * a - B_count * b) // c
    D_count = (A - A_count * a - B_count * b - C_count * c) // d
    print(A_count, B_count, C_count, D_count)