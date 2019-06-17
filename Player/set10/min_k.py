a1 = input().split()

if max(list(map(int,list(a1[0][0:int(a1[1])-1])))) < int(a1[1]):
    print("yes")
else:
    print("no")
