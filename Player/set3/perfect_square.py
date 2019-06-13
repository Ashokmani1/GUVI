a1 = list(map(int,input().split()))
i=0
x=0
while True:
    if (i *i) >= a1[0] and (i*i) <= a1[1]:
        x=x+1
    elif (i*i) > a1[1]:
        break
    i=i+1
print(x)
