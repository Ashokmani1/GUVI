from collections import Counter
a1 =int(input())
a2 = list(map(int,input().split()))
c = Counter(a2)
c2 = list(c.values())
print(max(c2))
