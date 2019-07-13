n1=list(map(str,input()))
for i in range(len(n1)):
    if n1.count(n1[i])>1 and n1[i]!=" ":
        print(n1[i].capitalize(),end="")
    else: print(n1[i],end="")
