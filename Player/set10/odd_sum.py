a1 = list(map(int,input().split()))
x=a1[0]
if a1[0]%2 == 0:
    x=a1[0]+1
a=0
for i in range(x,a1[1],2):
    a = a+i
print(a)
