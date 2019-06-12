a3=['/','%']
while True:
    a2=input().split()
    if a3.index(a2[1]) ==0:
        print(int(int(a2[0]) / int(a2[2])))
    else:
        print(int(a2[0]) % int(a2[2]))
