def solution(x):
    sum_ = 0
    
    for i in str(x):
        sum_ += int(i)
    if x % sum_ == 0:
        return True
    else:
        return False