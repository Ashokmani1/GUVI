a1=int(input())
l=[]
for i in range(1,a1+1):
    if a1%i == 0:
        l.append(i)
print(' '.join(map(str, l)))
