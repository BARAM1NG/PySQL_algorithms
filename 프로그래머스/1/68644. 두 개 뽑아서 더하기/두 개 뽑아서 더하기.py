def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            a = numbers[i] + numbers[j]
            answer.append(a)
    
    answer = list(set(answer))
        
    return sorted(answer)