def solution(k, score):
    answer = []
    que = []
    for i in range(len(score)):
        if len(que) < k:
            que.append(score[i])
            que.sort(reverse = True)
            answer.append(que[-1])
        else:
            que.append(score[i])
            que.sort(reverse = True)
            que.pop()
            answer.append(que[-1])
    return answer