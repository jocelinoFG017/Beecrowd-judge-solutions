#Author: Jocelino F.G


A,B,C= list(map(float, input().split()))

pi = 3.14159

tri = (A*C)/2
cir = (C*C*pi)
tra = ((A+B)*C)/2
qua = (B*B)
ret = (A*B)

print("TRIANGULO: %0.3f" % tri)
print("CIRCULO: %0.3f" % cir)
print("TRAPEZIO: %0.3f" % tra)
print("QUADRADO: %0.3f" % qua)
print("RETANGULO: %0.3f" % ret)