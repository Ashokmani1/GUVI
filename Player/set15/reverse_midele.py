a1 = input().split()
for i in range(0,len(a1)):
    if i == 0 or (len(a1) -1) == i:
        print(a1[i],end=' ')
    else:
        print(a1[i][::-1],end=' ')
        
    
