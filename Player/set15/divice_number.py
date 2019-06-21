a3 = int(input())
a2 = list(map(int , input().split()))
for i in range(0,len(a2)-1):
    if a2 [i+1] % a2[i] == 0:
        print(a2[i+1],end=' ')
