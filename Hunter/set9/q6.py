from collections import OrderedDict
str4=input()

def remove_duplicate(str4):
    return "".join(OrderedDict.fromkeys(str4))
str2="".join(OrderedDict.fromkeys(str4))
str3=str2[::-1]
print (str3)
