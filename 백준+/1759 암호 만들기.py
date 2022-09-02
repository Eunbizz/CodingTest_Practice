from itertools import combinations
import sys
input = sys.stdin.readline

l, c = map(int, input().split())
a = list(map(str, input().split()))

a.sort()

com = combinations(a, l)

for str in com:
    m=0
    for i in range(l):
        if str[i] in "aeiou":
            m +=1
    if m >=1 and l-m >= 2:
        print(''.join(str)) #('a', 'c', 'i', 's') 이렇게 나오기 때문에 변환