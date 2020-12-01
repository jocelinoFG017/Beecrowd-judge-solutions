#Author: Jocelino F.G

a, b = input().split(), input().split()
q1 = int(a[1])
v1 = float(a[2])
q2 = int(b[1])
v2 = float(b[2])
t1 = q1 * v1
t2 = q2 * v2
tt = t1 + t2
print('VALOR A PAGAR: R$ %.2f' %tt)