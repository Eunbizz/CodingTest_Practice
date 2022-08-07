n = int(input())
numbers = map(int, input().split())
ans = 0

for i in numbers:
    if i != 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            ans += 1
            
print(ans)