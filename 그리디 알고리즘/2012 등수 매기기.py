import sys
n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))
    
num.sort()
result = 0

for i in range(1, n+1):
    result += abs(i-num[i-1])

print(result)       