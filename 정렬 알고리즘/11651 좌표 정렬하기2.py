n = int(input())
A = []
for _ in range(n):
    x, y = map(int, input().split())
    A.append((x,y)) 
A.sort(key = lambda x: (x[1], x[0])) 

for i in A:
    print(i[0], i[1])