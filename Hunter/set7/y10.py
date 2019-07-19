sa1=input()
che=True
if '@' not in sa1:
	che=False
if sa1.count('@')>1 or sa1.count('.')>1 and che==True:
	che=False
if len(sa1[sa1.index('@')+1:sa1.index('.')])<4 or sa1[sa1.index('@')+1:sa1.index('.')]!="gmail" and che==True:
	che=False
if len(sa1[:sa1.index('@')])<3 and che==True:
	che=False
if sa1.endswith('.com')==False and che==True:
	che=False
if che:
	print("YES")
else:
	print("NO")
