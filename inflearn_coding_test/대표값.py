N = int(input())
score = list(map(int, input().split()))

mean = round((sum(score) / N), 0)

n = 21470000000

for idx, x in enumerate(score):
    tmp = abs(mean-x)
    if tmp < n:
        n = tmp
        ans  = x # 차이가 작은 점수 저장
        res = idx + 1 # 차이가 작은 인덱스 저장
    elif tmp == n: # 같은 거리가 나올 때
        if x > ans:
            ans = x
            res = idx + 1
print(mean, res)
        

# 소수 첫째자리 반올림 - round
# N개의 점수의 평균 중 가장 가까운 점수의 인덱스 출력
# 두 개일 경우 높은 점수의 인덱스 출력
# 답이 되는 점수가 여러 개일 경우 번호가 빠른 점수의 인덱스 출력

# 조건이 많아서 어려움
# enumerate로 인덱스와 값 대응
# 같이 저장하면서 움직이기 


