# 사전 풀이
# card의 숫자들을 dict의 key, 목표를 value로 하여 사전을 만든다
# target 숫자들을 key로 하여 value를 출력한다

n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
targets = list(map(int, input().split()))
dic = dict()

for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        
for i in range(m):
    if targets[i] in dic:
        print(dic[targets[i]], end = ' ')
    else:
        print(0, end = ' ')