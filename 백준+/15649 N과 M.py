from itertools import permutations
n, m = map(int, input().split())

nlist = [i for i in range(1, n+1)]
list(permutations(nlist))