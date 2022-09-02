from itertools import permutations

n = int(input())
A = list(map(int, input().split()))

ans = -1 # 답 변수를 초기화
for p in list(permutations(A)):
    sum = 0
    for i in range(n-1):
        sum += abs(p[i]-p[i+1]) # 인접한 수의 차 절댓값
    if ans < sum:
        ans = sum
print(ans)
