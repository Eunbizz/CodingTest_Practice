n = int(input())
a = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if a[i-1] > a[i]:
        for j in range(n-1,0,-1):
            if a[i-1] > a[j]:
                a[i-1], a[j] = a[j], a[i-1]
                a = a[:i] + sorted(a[i:], reverse=True) #큰애를 기준으로 뒤에는 리버스 정렬
                print(*a)
                exit()
print(-1)