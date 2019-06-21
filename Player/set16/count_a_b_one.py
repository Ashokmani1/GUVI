a1 = input()
if (a1.count('a')+a1.count('b') == len(a1)) or a1.count('a') == len(a1) or a1.count('b') == len(a1) or (len(a1)) -(a1.count('a')+a1.count('b')) == 1:
    print("yes")
else:
    print("no")
