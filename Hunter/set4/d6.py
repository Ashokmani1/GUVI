N1 = input()
b = []
for i in N1:
  b.append(int(i))
cc1 = str(sum(b))
if(cc1 == cc1[::-1]):
  print("YES")
else:
  print("NO")
