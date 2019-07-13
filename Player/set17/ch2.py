rn,rm=map(int,input().split())
rg=min(rn,rm)
rc=1
for i in range(1,rg+1):
	rc*=i
print(rc)
