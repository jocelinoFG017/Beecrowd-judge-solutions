#Author: Jocelino F.G

A = float(input())

N = A

a = int(N/100)
b = N%100
c = int(b/50)
d = b%50 
e = int(d/20)
f = d%20
g = int(f/10)
h = f%10
i = int(h/5)
j = h%5
k = int(j/2)
l = int(j%2)
  
E = A*100
B = int(E)
m = B%100
n = int(m/50)
o = m%50
p = int(o/25)
q = o%25
r = int(q/10)
s = q%10
t = int(s/5)
u = int(s%5)

print("NOTAS:")

print("{} nota(s) de R$ 100.00".format(a))
print("{} nota(s) de R$ 50.00".format(c))
print("{} nota(s) de R$ 20.00".format(e))
print("{} nota(s) de R$ 10.00".format(g))
print("{} nota(s) de R$ 5.00".format(i))
print("{} nota(s) de R$ 2.00".format(k))

print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(l))
print("{} moeda(s) de R$ 0.50".format(n))
print("{} moeda(s) de R$ 0.25".format(p))
print("{} moeda(s) de R$ 0.10".format(r))
print("{} moeda(s) de R$ 0.05".format(t))
print("{} moeda(s) de R$ 0.01".format(u))
  
  