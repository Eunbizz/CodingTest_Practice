n = int(input())
N = list(map(int, input().split()))

for i in sorted(list(set(N))):
    print(i, end = ' ')