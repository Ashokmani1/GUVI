a2=int(input())
i=0
while True:
  if a2 == (2**i):
    print("yes")
    break
  elif a2 < (2**i):
    print("no")
    break
  i=i+1
