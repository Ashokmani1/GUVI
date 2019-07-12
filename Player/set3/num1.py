x4,y4=map(int,input().split())
x5,y5=map(int,input().split())
x6,y6=map(int,input().split())
a = x4 * (y5 - y6) + x5 * (y6 - y4) + x6 * (y4- y5) 
if(a==0):
    print("yes")
else:
    print("no")
