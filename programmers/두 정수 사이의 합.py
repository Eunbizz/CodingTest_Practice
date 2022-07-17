def solution(a, b):
    answer = 0
    x = min(a,b)
    y = max(a,b)
    
    for i in range(y-x+1):
        if x == y:
            answer = x
        else:
            answer = answer + x + i
            if x + i == y:
                break
    return answer

# 다른 사람 코드
def solution(a, b):
    if a > b:
        a, b = b, a
    answer = sum(range(a, b+1))
    return answer
