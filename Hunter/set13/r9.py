st1,st=input().split()
for i in st1:
    for j in st:
        if(i==j):
            res=set(j)
            print(*res,end="")
