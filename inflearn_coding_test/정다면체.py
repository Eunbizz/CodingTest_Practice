N, M = map(int, input().split())

cnt = [0] * (N+M+1)  # cnt 초기화

for i in range(1, N+1):
    for j in range(1, M+1):
        cnt[i+j] += 1

max  = 0
# 여기가 막혔음
# cnt에서 가장 큰 점수의 인덱스를 구하는 부분(중복 있음)
for i in range(N+M+1):
    if max < cnt[i]:
        max = cnt[i]  # max 점수만 구하면 됨

for i in range(N+M+1):
    if cnt[i] == max:
        print(i, end=' ') # 한 칸 띄고 출력
        





