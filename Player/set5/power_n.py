a1 = list(map(int,input().split()))
i=1
while True:
    if (a1[1]*i) == a1[0]:
        print("yes")
        break
    elif (i*i) > a1[0]:
        print("no")
        break
    i=i+1
