N = int(input())
num = list(map(int, input().split()))
  
def digit_sum(x):
    sum = 0
    while x > 0:  # 자릿수의 합 
        sum += x%10
        x = x//10
    return sum

max = 0 

for x in num:
    total = digit_sum(x)
    if total > max:
        max = total
        res = x
print(res)