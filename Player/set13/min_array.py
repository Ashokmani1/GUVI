a1 = int(input())
a2 = list(map(int,input().split()))
x=0
for i in a2:
  if i < 0:
    x=x+i
print(x)
