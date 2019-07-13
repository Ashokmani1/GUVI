b2=int(input())
a1=list(map(int,input().split()))
c1=list(map(int,input().split()))
if(c1[::]==a1[::-1]):
    print("yes")
else:
    print("no")
