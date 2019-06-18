a1 = list(input())
a2 = list(map(int,a1))
x=0
for i in a2:
  if i % 2 != 0:
    x=x+i
if x % 2==0:
  print("E")
else:
  print("O")
