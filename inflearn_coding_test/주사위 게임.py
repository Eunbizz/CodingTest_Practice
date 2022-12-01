N = int(input())
res = 0

for i in range(N):
    tmp = input().split() # 리스트 문자로 들어옴
    tmp.sort()
    
    a, b, c = map(int, tmp)
    if a == b and b == c:
        mon = 10000 + a * 1000
    elif a == b or a == c:
        mon = 1000 + a * 100
    elif b == c:
        mon = 1000 + b * 100
    else:
        mon = c*100
    if mon > res:
        res = mon
    
print(res)
            
        
        
# 같은 눈이 세 개 나오는지 확인 어케하지?