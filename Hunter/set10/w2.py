s1=input()
n=1
if len(s1)==1:
    print("yes")
else:
    for j in s1:
        if s1.count(j)==len(s1):
            print("no")
            n=0
            break
    if n==1:
        print("yes")
