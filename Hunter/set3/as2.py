b=int(input())
lst1=list(map(int,input().split()))
re1=1
len=[]
for i in lst1:
  re1=re1*i
for i in lst1:
  len.append(re1//i)
