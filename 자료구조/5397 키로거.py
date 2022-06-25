test_case = int(input())

for _ in range(test_case):
    left_s = []
    right_s = []
    data = input()
    for i in data:
        if i == '-':
            if left_s:
                left_s.pop()
        elif i == '<':
            if left_s:
                right_s.append(left_s.pop())
        elif i == '>':
            if right_s:
                left_s.append(right_s.pop())
        else:
            left_s.append(i)
    left_s.extend(reversed(right_s)) # 왼쪽 스택에 오른쪽 스택 딱 붙이기 위해 reversed
    print(''.join(left_s)) # 공백 없이 출력
     
            