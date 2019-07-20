n = int(input())
x1 = list(map(int, input().split()))
for i in range(len(x1)):
    if i == n-1:
        print(-1, end="")
    else:
        if x1[i] > x1[i+1]:
            print(x1[i+1], end=" ")
        else:
            print(-1, end=" ")
