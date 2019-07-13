str1=input()
str3=input()
arr=[]
if (str1.isalpha() or " " in str1) and (str3.isalpha() or " " in str3):
    str1=list(str1.split(" "))
    str3=list(str3.split(" "))
    for i in str1:
        if str1.count(i) > str3.count(i) and i not in arr:
            arr.append(i)
    for i in str3:
        if str3.count(i)>str1.count(i) and i not in arr:
            arr.append(i)
    print(*arr)
else:
    for i in str1:
        if str1.count(i)>str3.count(i) and i not in arr:
            arr.append(i)
    for j in str3:
        if str3.count(j)>str1.count(j) and j not in arr:
            arr.append(j)
    print(*arr)
