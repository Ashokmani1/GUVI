a2=input()
if len(a2) == 1:
	print("10")
else:
    print(str(int(a2[0:len(a2)-1])+1) + "0")
