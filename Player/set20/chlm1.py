b1=input()
b1=b1.split()
w2=str(b1[0])
w1=str(b1[1])
if((w2=='R' or w2=='P') and (w1=='P' or w1=='R')):
    if(w2==w1):
        print("D")
    else:
        print("P")
elif((w2=='P' or w2=='S') and (w1=='S' or w1=='P')):
    if(w2==w1):
        print("D")
    else:
        print("S")
elif((w2=='R' or w2=='S') and (w1=='S' or w1=='R')):
    if(w==w1):
        print("D")
    else:
        print("R")
