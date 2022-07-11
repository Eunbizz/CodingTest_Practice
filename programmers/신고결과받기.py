# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = [0] * len(id_list) 
    reports = {x : 0 for x in id_list} #아이디와 value=0으로 채운 딕셔너리 만들기
    
    for r in set(report): 
        reports[r.split()[1]] += 1 #신고자와 신고당한사람 아이디 분리하고 신고당한 수 세기
    
    for r in set(report):
        if reports[r.split()[1]] >= k: #신고당한 수가 k번 이상이면 
            answer[id_list.index(r.split()[0])] += 1 #id_list 값 중에 신고자가 있는 index와 같은 answer index + 1 해준다
                
                
    return answer