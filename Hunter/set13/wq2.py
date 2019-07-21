n=int(input())
li1=[int(i) for i in input().split()]
n2=0
for i in range(0,len(li1)):
    if li1.count(li[i])>n2:
        n2=li1.count(li1[i])
        a=li1[i]
print(a)
