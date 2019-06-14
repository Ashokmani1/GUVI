a1  = int(input())
a2 = input().split()
a3 = input().split()
for i in a2:
    if a3.count(i) > 0 :
        print(i,end=' ')
        x = a3.index(i)
        a3.pop(x)
        
    
