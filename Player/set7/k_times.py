from collections import Counter
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
c = Counter(a2)
c1 = list(c.keys())
c2 = list(c.values())
x=0
if c2.count(a1[1]) == 1:
   x = c1[c2.index(a1[1])]
print(x)
