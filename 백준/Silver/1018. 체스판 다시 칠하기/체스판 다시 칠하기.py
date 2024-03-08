def solution(board):
    '''
    첫 체스가 B
    row: 짝수 index는 col이 짝수
      홀수 index는 col이 홀수
    '''
    # print(board)
    countB, countW = 0, 0
    for i in range(8):
        for j in range(8):
            if (i%2==0 and j%2==0 and board[i][j]!='B') or \
              (i%2==0 and j%2!=0 and board[i][j]!= 'W'):countB += 1
            elif (i%2!=0 and j%2!=0 and board[i][j]!='B') or \
              (i%2!=0 and j%2==0 and board[i][j]!='W'): countB += 1
            if (i%2==0 and j%2==0 and board[i][j]!='W') or \
              (i%2==0 and j%2!=0 and board[i][j]!= 'B'): countW += 1
            elif (i%2!=0 and j%2!=0 and board[i][j]!='W') or \
              (i%2!=0 and j%2==0 and board[i][j]!='B'): countW += 1

    return min(countB, countW)

    

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

answer = float('inf')
count = 0
for i in range(N):
    for j in range(M):
        if N-i >= 8 and M-j >= 8:
            tmp = [row[j:8+j] for row in board[i:i+8]]
            answer = min(solution(tmp), answer)
            
print(answer)