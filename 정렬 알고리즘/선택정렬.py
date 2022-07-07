# 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꿈
# n-1번 반복

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i #가장 작은애의 위치
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j #끝까지 다 보고 가장 작은 애를 설정
    array[i], array[min_index] = array[min_index], array[i] #스와프

print(array)