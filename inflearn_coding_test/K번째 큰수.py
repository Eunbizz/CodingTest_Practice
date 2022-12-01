N, K = map(int, input().split())
num = list(map(int, input().split()))

res = set()
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            res.add(num[i] + num[j] + num[k])
res = list(res)
res.sort(reverse=True)
print(res[K-1])


# N장의 카드 중 3장을 뽑아 합한 값을 모두 기록
# 그 중 K번째로 큰 수를 출력
# 중복될 때는 한 번만 카운팅 해야 함 -> set 자료구조 사용(중복을 제거)
# set 은 append가 아닌 add
# set는 sort 기능 없음
# list로 변경해야 함

# 3장씩 더하는 모든 경우를 어케 구하지..
# -> 3중 for 문!!!