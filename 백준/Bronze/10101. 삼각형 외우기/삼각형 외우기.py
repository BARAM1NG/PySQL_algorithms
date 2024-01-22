A_list = []

for i in range(3):
    a = int(input())
    A_list.append(a)

if sum(A_list) != 180:
    print('Error')
elif A_list[0] == A_list[1] == A_list[2]:
    print('Equilateral')
elif (A_list[0] == A_list[1]) or (A_list[1] == A_list[2]) or (A_list[2] == A_list[0]):
    print('Isosceles')
else:
    print('Scalene')