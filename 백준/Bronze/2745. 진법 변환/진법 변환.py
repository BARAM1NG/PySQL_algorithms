N, B = input().split()
B = int(B)

alphabet_list = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
num_list = list(range(36))

sum = 0

for i, char in enumerate(N):
    num_index = alphabet_list.index(char)
    sum += (num_list[num_index] * (B ** (len(N) - 1 - i)))
    
print(sum)