a=['a','e','i','o','u']
x=input()
if a.count(x) != 0:
  print("Vowel")
elif x.isalpha():
  print("Consonant")
else:
  print("invalid")
