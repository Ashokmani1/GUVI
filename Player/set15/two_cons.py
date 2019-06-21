a1 = int(input())
a2 = []
a2.append(input())
x=0
for i in range(1,a1-1):
    a2.append(input())
    if a2[i] == a2[i-1]:
        print("yes")
        x= x+1
        break
if x == 0:
    print("no")
