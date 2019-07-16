from itertools import permutations
c1=input()
d1=permutations(c1)
for i in list(d1):
    print("".join(i))
