l1 = []
l1 = input().split()
l2 = []
for i in range(len(l1)):
    s = l1[i]
    a = s[::-1]
    l2.append(a)
print(*l2, sep=" ")
