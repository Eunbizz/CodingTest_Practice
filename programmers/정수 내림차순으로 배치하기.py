def solution(n):
    answer = [int(i) for i in str(n)]
    answer.sort(reverse=True)
    dap = ''
    for i in answer:
        dap += str(i)
    return int(dap)

# 다른 사람 풀이
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))