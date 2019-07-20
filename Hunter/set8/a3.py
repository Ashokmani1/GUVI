rb1 = input()
bs = input()
s = ""
for i in range(len(rb1)):
  for j in range(len(rb1),-1,-1):
    if rb1[i:j] in bs:
      if len(rb1[i:j])>=len(s):
        s=rb1[i:j]
print(s)
