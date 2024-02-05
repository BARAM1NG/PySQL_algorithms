N_list = [int(input()) for _ in range(9)]

N_list.sort()

sum_ = sum(N_list)


for i in range(len(N_list)):
  for j in range(i + 1, len(N_list)):
    if sum_ - N_list[i] - N_list[j] == 100:
      for k in range(len(N_list)):
        if k == i or k ==j:
          pass
        else:
          print(N_list[k])
      exit()