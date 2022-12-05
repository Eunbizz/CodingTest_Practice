n, m = map(int, input().split())
s = list(map(int, input().split()))

p1 = 0
p2 = 1
cnt = 0
sum = s[0]

while True:
    if sum < m: 
        if p2 < n:
            sum += s[p2]
            p2+=1
        else:
            break
    elif sum == m: 
        cnt += 1
        sum -= s[p1]
        p1 += 1
    else:
        sum -= s[p1]
        p1 += 1
print(cnt)
        
        

print(cnt)