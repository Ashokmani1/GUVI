a2= int(input())
a1 = list(map(int,input().split()))
x=a1[0]
for i in range(1,len(a1)):
    x=x^a1[i]
print(x)
    
