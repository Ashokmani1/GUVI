    
e=input()
l=[]
for i in e:
    if(i.isnumeric()):
           l.append(i)
print(*l,sep="")
