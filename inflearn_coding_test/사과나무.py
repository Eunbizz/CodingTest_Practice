N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
tot = 0
s = e = N//2

for i in range(N):
    for j in range(s, e+1):
        tot += a[i][j]
    if i < N//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(tot)