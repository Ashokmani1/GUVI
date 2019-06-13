a2 =int(input())
a1 = list(map(int,input().split()))
a3 =a1[:]
a3.sort()
if a1 == a3:
    print("yes")
else:
    print("no")
