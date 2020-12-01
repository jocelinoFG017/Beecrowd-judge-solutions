d = input().split()
a, b, c = d

a = float(a)
b = float(b)
c = float(c)

perimetro = 0
area = 0
 
if ((b-c) < a < (b+c)) and ((a-c)< b <(a+c))and((a-b)< c <(a+b)):
    perimetro = a+b+c
    print("Perimetro = ", perimetro)
else:
    area = (c *(a+b))/2
    print("Area = ", area)
