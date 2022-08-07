m, n = map(int, input().split())
ans = []

for i in range(m, n+1):
    if i != 1:
        for j in range(2, int(i**0.5)+1): #i까지 하면 시간초과! i의 제곱근까지만 바줘도 답 나옴
            if i % j == 0:
                break
        else:
            ans.append(i)
        
for i in ans:
    print(i)