x,y,z=map(int,input().split())
count1=0
for i in range(x,y+1):
   if str(z)in str(i):
       count1+=1
print(count1)
