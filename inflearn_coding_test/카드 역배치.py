ans = list(range(21))
for _ in range(10):
    a, b = map(int, input().split())
    
    for i in range((b-a+1)//2):
        ans[a+i], ans[b-i] = ans[b-i], ans[a+i]
ans.pop(0)

for x in ans:
    print(x, end = ' ')