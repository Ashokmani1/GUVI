n1=list(map(str,input()))
k1=list(map(str,input()))
for i in range(len(k1)):
    n1.append(k1[i])
if len(set(n1))==26: print("complementary")
else: print("non-complementary")
