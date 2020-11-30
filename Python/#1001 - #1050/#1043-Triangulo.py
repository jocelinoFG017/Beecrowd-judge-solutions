d = input().split()
a, b, c = d

a = float(a)
b = float(b)
c = float(c)

if ((b-c) < a < (b+c)) and ((a-c)< b <(a+c))and((a-b)< c <(a+b)):
    print("Perimetro = {:.1f}".format(a+b+c))
else:
    print("Area = {:.1f}".format((c *(a+b))/2))

