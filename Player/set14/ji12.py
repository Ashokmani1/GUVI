import sys
n1,k=map(int,input().split())
l=[]
for i in range(0,n1):
    l.append(list(map(int,input().split())))
for i in range(0,n1):
    if l[i][1]==k:
        print("yes")
        sys.exit()
print("no")
