from itertools import permutations

n = int(input())
nlist = [i for i in range(1, n+1)]

for num in list(permutations(nlist)):
    for j in num: # num을 프린트하면 (1,2,3) 이런식으로 나오기 때문에 필요
        print(j, end=' ')
    print()
    
