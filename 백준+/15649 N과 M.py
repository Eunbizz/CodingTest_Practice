import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def get_seq(level ,seq): # 레벨은 M의 개수를 나타냄
    if level == M:
        print(' '.join(list(map(str, seq))))
        return
    
    for i in range(1, N+1):
        if i not in seq: # 숫자가 중복되지 않기 위해
            temp = seq.copy() # 임시 리스트
            temp.append(i)
            get_seq(level+1, temp)
get_seq(0,[])