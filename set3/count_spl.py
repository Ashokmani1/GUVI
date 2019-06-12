a1=input()
x=0
c=0
for i in range(0,len(a1)):
    if a1[i].isalpha() or a1[i].isdigit() or a1[i] == ' ':
        x=x+1 
    else:
        c=c+1
print(c)
