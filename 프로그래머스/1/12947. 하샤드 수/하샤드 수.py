def solution(x):
    
    x_list = list(str(x))
    
    num = 0
    
    for i in x_list:
        num += int(i)
    
    if x % num == 0:
        answer = True
    else:
        answer = False
    
    
    return answer