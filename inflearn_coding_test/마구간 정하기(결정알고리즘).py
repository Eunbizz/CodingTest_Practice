def Count(mid):
    cnt = 1
    ep = L[0]
    for i in range(1, n):
        if L[i] - ep >= mid:
            cnt += 1
            ep = L[i]
    return cnt
    
n, c = map(int, input().split())
L = []
for _ in range(n):
    tmp = int(input())
    L.append(tmp)

L.sort()

lt = 1
rt = max(L)

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid +1
    else:
        rt = mid -1
print(res)