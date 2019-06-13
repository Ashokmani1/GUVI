l1= [2,1,1,1,1]
l2 = ['a','b','i','k','l']
a2 = int(input())
for i in range(0,a2):
    a3 = input()
    x,y=0,0
    for i in range(len(l2)):
        if a3.count(l2[i]) == l1[i]:
            x=x+1
    if x == 5:
        y = y + 1
print(y)
