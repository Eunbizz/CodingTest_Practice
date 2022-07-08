from collections import Counter

N = int(input())
s_card = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

count = Counter(s_card)

for i in range(len(card)):
    if card[i] in s_card:
        print(count[card[i]], end = ' ')
    else:
        print(0, end = ' ')