def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]
# remove 함수 기억하기!