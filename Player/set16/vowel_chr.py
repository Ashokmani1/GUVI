a1 = input()
a2 = ['a','e','i','o','u']
x=0
for i in range(0,len(a1)-1):
        if (a1[i] not in a2 and a2.count(a1[i+1]) == 1) or (a1[i+1] not in a2  and a2.count(a1[i]) == 1):
            x=x+1
print(x)
