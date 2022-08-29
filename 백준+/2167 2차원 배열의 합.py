n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

psum = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        psum[i][j] = a[i-1][j-1] + psum[i][j-1] + psum[i-1][j] - psum[i-1][j-1]


k = int(input())
for i in range(k):
    i, j, x, y = map(int, input().split())
    print(psum[x][y] - psum[x][j-1] - psum[i-1][y] + psum[i-1][j-1])
