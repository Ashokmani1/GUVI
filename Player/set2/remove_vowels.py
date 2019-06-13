a2= int(input())
li=['a','e','i','o','u']
name1 = input()
for i in range(0,len(li)):
    name1 = name1.replace(li[i],'')
print(name1)
