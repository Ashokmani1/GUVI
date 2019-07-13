aa1,bb1,cc1=map(int,input().split())
if (aa1**2)+(bb1**2)==cc1**2 or (bb1**2)+(cc1**2)==aa1**2 or (aa1**2)+(cc1**2)==bb1**2:
	print("yes")
else:
	print("no")
