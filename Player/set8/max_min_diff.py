a1= int(input())
a2 = list(map(int,input().split()))
a2.sort()
print(max(a2)-min(a2))
