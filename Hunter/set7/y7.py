a1=int(input())
bb=list(map(str,input().split()))[:a1]
cc=input()
dd=0
for i in range(0,a1):
  if(bb[i].startswith(cc)):
    dd=dd+1
print(dd)
