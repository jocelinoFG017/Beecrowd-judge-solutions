
x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
if(a < b) and (b < c):
  print(a)
  print(b)
  print(c)
elif(a < c) and (c < b):
  print(a)
  print(c)
  print(b)
elif(b < a) and (a < c):
  print(b)
  print(a)
  print(c)
elif(b < c) and (c < a):
  print(b)
  print(c)
  print(a)
elif(c < a) and (a < b):
  print(c)
  print(a)
  print(b)
elif(c < b) and (b < a):
  print(c)
  print(b)
  print(a)
print('')
print(a)
print(b)
print(c)
