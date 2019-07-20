n1=int(input())
c=0
for i in range(n1+1):
    k1=str(i)
    if all(abs(int(k1[j])-int(k1[j-1]))==1 for j in range(1,len(k1))):
        c=c+1
print(c)
