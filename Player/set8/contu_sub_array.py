a2 = int(input())
a1 =list(map(int,input().split()))
x=1
for i in range(0,len(a1)-1):
    if a1[i] < a1[i+1]:
        x=x+1
    else:
        break
print(x)
