a1 = input().split()
if a1.count('and') > 0:
    try:
        x= a1.index('and')
        a1[x-1],a1[x+1] = a1[x+1],a1[x-1]
        print(' '.join(map(str,a1)))
    except:
        print(' '.join(map(str,a1)))
else:
    print(' '.join(map(str,a1)))
        
