a1 = input()
for i in a1:
    if ord(i) > 64  and ord(i) < 88 or ord(i) > 96 and ord(i) < 120:
        print(chr(ord(i)+3),end='')
    else:
        print(chr(ord(i)+3-26),end='')
        
