A_list = []

for _ in range(5):
    B_list = list(input())
    A_list.append(B_list)

for i in range(15):
    for j in range(5):
        if i < len(A_list[j]):
            print(A_list[j][i], end = '')