a3 = int(input())
a1 = list(map(int , input().split()))
a2 = list(map(int , input().split()))
a3 = a2[:]
a3.sort()
for i in a3:
    print(a1[a2.index(i)],end=' ')
