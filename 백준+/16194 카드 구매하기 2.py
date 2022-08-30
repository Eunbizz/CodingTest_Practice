n = int(input())
c = [0]
c += list(map(int, input().split()))
dp = [0] * 1001

for i in range(1, n+1):
    dp[i] = c[i]
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j] + c[j])
print(dp[n])