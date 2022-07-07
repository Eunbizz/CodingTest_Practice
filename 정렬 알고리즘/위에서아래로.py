#내림차순으로 정렬하는 프로그램
n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort(reverse = True)

for i in array:
    print(i, end=' ')
    
    