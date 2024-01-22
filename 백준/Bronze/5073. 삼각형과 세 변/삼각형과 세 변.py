while True:
    a = list(map(int, input().split()))
    if sum(a) == 0:
        break 
    
    if max(a) >= sum(a) - max(a):
        print('Invalid')
    elif len(set(a)) == 1:
        print('Equilateral')
    elif len(set(a)) == 2:
        print('Isosceles')
    else:
        print('Scalene')