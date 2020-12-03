aux=0
soma=0
for x in range(1,7):
    numero = float(input())
    if(numero>0):
        soma = soma + numero
        aux= aux + 1
print(aux,"valores positivos")
print("{:.1f}".format(soma/aux))