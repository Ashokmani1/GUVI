a1=input().split()
for i in range(0,len(a1)):
    if a1[i][0].isdigit():
        print(a1[i],end=' ')
    else:
        if (a1[i][0].isupper()):
            print(a1[i],end=' ')
        else:
            print(chr(ord(a1[i][0])-32)+a1[i][1:len(a1[i])],end=' ')
        
