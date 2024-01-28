N, k = map(int, input().split())

N_list = list(map(int, input().split()))

N_list.sort(reverse = True)

print(N_list[k - 1])