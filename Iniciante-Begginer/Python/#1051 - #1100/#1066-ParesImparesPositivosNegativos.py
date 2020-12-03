par=0
impar=0
negativo = 0
positivo = 0
for x in range(1,6):
    numero = int(input())
    if(numero % 2 == 0):
        par= par + 1
    else:
        impar = impar +1
    if numero >0:
        positivo = positivo + 1
    elif numero < 0:
        negativo = negativo +1

print(par, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(positivo, "valor(es) positivo(s)")
print(negativo, "valor(es) negativo(s)")
