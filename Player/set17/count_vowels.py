    
a1 =int(input())
a2 = []
a3 = ['a','e','i','o','u']
k=0
for i in range(0,a1):
    a2.append(list(input()))

    for j in a2[i]:
        if j in a3:
            k = k+1
            break

if k == a1:
    print("yes")
else:
    print("no")
