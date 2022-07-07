#이코테 180p

n = int(input())
array = []
for _ in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key = lambda data: data[1]) 
for data in array:
    print(data[0], end=' ')