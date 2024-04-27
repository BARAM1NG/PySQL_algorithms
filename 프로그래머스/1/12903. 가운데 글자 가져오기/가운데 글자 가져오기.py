def solution(s):
    if len(s) % 2 == 0:
        a = int(len(s) / 2)
        answer = s[a - 1: a + 1]
    else:
        a = int(len(s) / 2)
        answer = s[a]
        
    return answer