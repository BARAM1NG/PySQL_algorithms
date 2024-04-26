def solution(x, n):
    
    answer = []
    x_first = x
    
    for _ in range(n):
        answer.append(x)
        x += x_first
        
    return answer