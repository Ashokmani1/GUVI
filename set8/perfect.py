a1=list(map(int,input().split()))
i=0
x=0
while True:
   if (a1[1] * a1[0])  == (i*i):
       print("yes")
       x=x+1
       break
   if (a1[1] * a1[0]) < (i*i):
       print("no")
       break
   i=i+1
