a1 = input().split()
a2 = input().split()
for i in a2:
  a1.remove(i)
print(' '.join(map(str,a1)))
