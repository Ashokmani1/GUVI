import math
a4 =  int(input())
a1 = list(map(int , input().split()))
if len(a1) % 2 == 0:
    a2 = a1[0:math.floor(len(a1)/2)]
    a2.sort()
    a3 = a1[math.floor(len(a1)/2):len(a1)]
    a3.sort(reverse = True)
    print(' '.join(map(str,a2+a3)))
else:
    a2 = a1[0:math.floor((len(a1)-1)/2)]
    a2.sort()
    a3 = a1[math.floor((len(a1)-1)/2):len(a1)]
    a3.sort(reverse = True)
    print(' '.join(map(str,a2+a3)))
