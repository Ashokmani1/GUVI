inp=int(input())                       
val=list(map(int,input().split()))   
final=[]
for i in range(len(val)):
    if i == val[i]:                
        final.append(str(val[i]))
if len(final)!=0:
    print(" ".join(final))               
else:
    print('-1')
