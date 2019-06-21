a1 =list(map(int,input().split()))
a2 = []
a2.append(input())
x=1
i=0
for i in range(1,a1[0]):
    a2.append(input())
    if a2[i] == a2[i-1]:
        x= x+1
    else:
        x = 1
    if x == a1[1]:
        print("yes")
        i = i+1
        break
if i == 0:
    print("no")
