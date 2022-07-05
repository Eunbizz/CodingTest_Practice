import sys

n = int(input())
array = []

for _ in range(n):
    array.append(int(sys.stdin.readline()))

for i in sorted(array):
    sys.stdout.write(str(i) + '\n')