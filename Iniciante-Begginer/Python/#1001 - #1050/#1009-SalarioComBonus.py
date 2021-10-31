# Author: Jocelino F.G
nome = input()
salario = float(input())
vendas = float(input())

comissao = salario + (15*vendas)/100

print("TOTAL = R$ %0.2f" % comissao)
