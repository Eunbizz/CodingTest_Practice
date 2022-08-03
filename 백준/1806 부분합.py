
n, m = map(int, input().split())
data = list(map(int, input().split()))

result = []
e = 0
sum = 0

for s in range(n):
    while sum < m and e < n: 
        sum += data[e]
        e += 1
    if sum == m:
        result.append(e-s)
    sum -= data[s]
print(min(result))
