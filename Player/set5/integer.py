n1=int(input())
if(n1>=-2**15+1 and n1<=2**15+1):
  print('INT')
elif(n1>=-2**31+1 and n1<=2**31+1):
  print('LONG')
else:
  print('LONG LONG')  
