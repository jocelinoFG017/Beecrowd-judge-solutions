X = int(input())
Y = int(input())
soma = 0
if X % 2 == 0:
    for i in range(X, Y, -1):
        if i % 2 != 0:
            soma = soma + i
else:
    X -= 1
    for i in range(X, Y, -1):
        if i % 2 != 0:
            soma = soma + i
print(soma)
