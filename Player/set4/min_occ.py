a1 = list(input())
for i in a1:
    if i != ' ':
        if a1.count(i) == 1:
            print(i.lower(),end=' ')
