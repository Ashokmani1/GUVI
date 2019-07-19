st,nn1=input().split()

st=str(st)  

nn1=int(nn1)

li=[] 

for i in range(len(st)-nn1+1):

	li.append(st[i:i+nn1]) 
  
print(*li)
