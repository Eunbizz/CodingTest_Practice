
T = int(input())
for i in range(T):
    N, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))

    num = num[s-1:e]
    num.sort()
    print("#%d %d" %(i+1, num[k-1]))

# 테스트 케이스가 여러 개인 문제 
# 하나의 테스트 케이스가 여러줄로 들어옴
# num = num.sort()로 하였더니 오류가 남
# print 문 주목