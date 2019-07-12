def catalan(nnn):
    if nnn<=1:
        return 1
    else:
        sss=0
        for i in range(nnn):
            sss=sss+catalan(i)*catalan(nnn-i-1)
        return sss
mm=int(input())
if mm==0:
    mm=1
c=[]
for i in range(mm):
    c.append(catalan(i))
print(*c)
