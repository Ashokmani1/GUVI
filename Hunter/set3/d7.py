alp=int(input())
h1=input()
a=list(map(int,h1.split()))
str1=""
a.reverse()
for i in a:
    str1+=str(i)+"->"
a=str1.strip('->')
print(a)
