# Author: Jocelino F.G.

n = int(input())
vetor = [n]

dobro = n
for i in range(0, 10):
    dobro = dobro * 2
    vetor.append(dobro)
    print("N[{}] = {}".format(i, vetor[i]))
