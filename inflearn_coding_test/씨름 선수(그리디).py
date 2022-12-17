n = int(input())
body = []
for _ in range(n):
    t, w = map(int, input().split())
    body.append((t,w))

body.sort(reverse=True)

cnt = 0
largest = 0

for x, y in body:
    if y > largest:
        largest = y
        cnt += 1
    
print(cnt)