idade = int(input())
media = 0
count = 0
soma = 0

while idade > 0:
    count += 1
    soma = soma + idade
    media = soma/count
    idade = int(input())

print("{:.2f}".format(media))
