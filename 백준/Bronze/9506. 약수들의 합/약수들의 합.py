while True:
    N = int(input())
    if N == -1: # 입력 값이 -1이면 반복문 종료
        break;
    N_list = []
    for i in range(1, N):
        if N % i == 0:
            N_list.append(i)
    if sum(N_list) == N:
        print(N, " = ", " + ".join(str(i) for i in N_list), sep="")
    else:
        print(N, "is NOT perfect.")