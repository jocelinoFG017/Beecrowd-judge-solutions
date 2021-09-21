op = int(input())
alc = 0
gas = 0
dis = 0

while op != 4:

    if op == 2:
        gas += 1
    elif op == 1:
        alc = alc + 1
    elif op == 3:
        dis = dis + 1
    op = int(input())

print("MUITO OBRIGADO")
print("Alcool: {}".format(alc))
print("Gasolina: {}".format(gas))
print("Diesel: {}".format(dis))
