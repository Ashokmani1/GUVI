import collections
a1 = list(input())
counter=collections.Counter(a1)
l=list(counter.values())
x=l.index(max(l))
l1=list(counter.keys())
print(l1[x])
