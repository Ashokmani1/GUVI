from collections import Counter
a1 = list(input())
a  = Counter(a1)
if max(list(a.values())) > 1:
    print("yes")
else:
    print("no")
