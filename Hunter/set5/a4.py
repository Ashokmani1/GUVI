rb1=input()

t=''

for i in range(0,len(rb1)-1,2):
  
  if int(rb1[i+1])%2==0:
    
    t+=rb1[i]*int(rb1[i+1])
    
  else:
    
    t+=rb1[i]+rb1[i+1]
    
print(t)
