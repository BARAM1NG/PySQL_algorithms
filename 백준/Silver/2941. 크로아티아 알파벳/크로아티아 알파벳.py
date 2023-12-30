S = input()
cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro_list:
    S = S.replace(i, '*')
    
print(len(S))