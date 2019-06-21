
i=0
a1 = int(input())
while True:
    if a1 == (2**i):
        print("yes")
        break
    if a1 < (2**i):
        print("no")
        break
    i = i+1
