a1 =list(map(int,input().split()))
length = a1[0]
width = a1[1]
height = a1[2]

SA = 2 * (length * width + length * height + width * height)

Volume = length * width * height

print(int(SA),int(Volume))
