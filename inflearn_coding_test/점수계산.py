N = int(input())
num = list(map(int, input().split()))

sum = 0 
cnt = 0

for i in num:
    if i == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)


# 가중치를 증가해가면서 sum에 누적
# 가중치가 포인또