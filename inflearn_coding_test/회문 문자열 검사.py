N = int(input())
for i in range(1, N+1):
    word = input()
    word = word.upper()
    size = len(word)
    
    for j in range(size//2):
        if word[j] != word[-1-j]:
            print('#%d No' %i)
            break
        
        else:
            print('#%d Yes' %i)
                