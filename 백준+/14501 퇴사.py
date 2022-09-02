n = int(input())

t = []
p = []
dp =  [0] * (n+1)

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)


for i in range(n-1, -1, -1):
    if t[i] + i > n: # 상담이 끝나는 날이 n을 넘어가면 일을 맡을 수 없기에
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i] + dp[i+t[i]])
print(dp[0])