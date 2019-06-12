a2 = input().split()
for i in range(0,len(a2)):
    if a2[i][0].isupper():
        print(a2[i],end=' ')
    else:
        print(chr(ord(a2[i][0])-32)+a2[i][1:len(a2[i])],end=' ')
