as1=input().split("#")
bs=input().split("#")
ds=as1[1]+as1[2]+as1[3]
es=bs[1]+bs[2]+bs[3]
if ds>es:
    print(as1[0])
elif es>ds:
    print(bs[0])
