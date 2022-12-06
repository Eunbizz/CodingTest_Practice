n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for _ in range(m):
    h, t, k = map(int, input().split())
    if t == 0: # 방향
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())    

tot = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        tot += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(tot)
            
           
    
