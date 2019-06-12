def is_isogram(word):
    if isinstance(word,str):
        w = word.lower() # assuming you want a case in-sensitive search
        return  len(w) == len(set(w)) if True else False
    

while True:
    if (is_isogram(input())):
        print("Yes")
    else:
        print("No")
