a1 = input()
x=0
for i in a1:
    if i.isdigit():
        x=x+1
if x == len(a1):
    print("yes")
else:
    print("no")
