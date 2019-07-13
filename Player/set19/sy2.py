n1=int(input())
v=['a','e','i','o','u','A','E','I','O','U']
cnt=0
a=[]
for i in range(n1):
    s1=input()
    for i in s1:
        if i in v:
            cnt+=1 
    a.append([s1,cnt])
    cnt=0
a.sort(key=lambda x:x[1],reverse=True)
for i in range(n1):
    print(a[i][0])
