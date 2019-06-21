import math
a4 =list(map(int , input().split()))
a1 = list(map(int , input().split()))
a2 = a1[0:a4[1]]
a2.sort()
a3 = a1[a4[1]:len(a1)]
a3.sort(reverse = True)
print(' '.join(map(str,a2+a3)))
