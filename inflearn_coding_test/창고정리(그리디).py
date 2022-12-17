l = int(input())
L = list(map(int, input().split()))
m = int(input())

L.sort()
for _ in range(m):
    L[l-1] -= 1
    L[0] += 1
    L.sort()
    
print(L[l-1] - L[0])