a=input().split()
b1=[]
for i in a:
  b1.append(i[::-1])
print(*b1)
