a2 = input().split()
for i in range(0,len(a2)):
    print(a2[i][0].upper()+a2[i][1:len(a2[i])].lower(),end=' ')
