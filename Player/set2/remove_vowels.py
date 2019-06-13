a2= int(input())
li=['a','e','i','o','u','A','E','I','O','U']
name1 = input()
for i in range(0,len(li)):
    name1 = name1.replace(li[i],'')
print(name1[::-1])
