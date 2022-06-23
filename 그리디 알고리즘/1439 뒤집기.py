s = input()

make1 = 0
make0 = 0

if s[0] == '1':
    make0 += 1       
else: 
    make1 += 1
    
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            make1 += 1
        else:
            make0 += 1
print(min(make1, make0))
        
    