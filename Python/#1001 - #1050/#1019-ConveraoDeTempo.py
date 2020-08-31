#Author: Jocelino F.G

x = int(input())

hora = x //3600
resto = x %3600

minutos = resto // 60
resto= resto % 60
seg = resto // 1
print("{}:{}:{}".format(hora, minutos, seg))