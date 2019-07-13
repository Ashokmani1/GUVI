p1=int(input())
q1=list(map(int,input().split()))
if len(q1)==p1:
    r=max(q1)
    s=min(q1)
    t=r-s
print(t)
