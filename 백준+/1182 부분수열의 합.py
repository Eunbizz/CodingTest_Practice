from itertools import combinations

N, S = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for num in range(1, N+1):
    for i in list(combinations(a, num)):
        if sum(i) == S:
            ans += 1
print(ans)

