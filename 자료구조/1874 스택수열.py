n = int(input())

count = 1
stack = []
result = []
temp = True

for i in range(n): 
    data = int(input())
    while count <= data: # 입력받은 데이터에 도달할 때까지 삽입
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data: # 스택의 최상위 원소가 데이터와 같을 때 출력
        stack.pop()
        result.append('-')
    else:
        temp = False
if temp == False:
    print('No')
else:
    for i in result:
        print(i)
