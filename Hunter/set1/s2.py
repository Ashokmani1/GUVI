alp=int(input())
h1=input()
s1=list(map(int,h1.split()))
if len(s1)==alp:
    s1.sort(reverse=True)
    k1=[str(i) for i in s1]
    m=int("".join(k1))
    print(m)
