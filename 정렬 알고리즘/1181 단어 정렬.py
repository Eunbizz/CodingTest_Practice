
n = int(input())
list_ = []

for _ in range(n):
    list_.append(input())
list_ = list(set(list_))

list_.sort() #사전순으로 정렬 
list_.sort(key = len) #길이순으로 정렬

for i in list_:
    print(i)
