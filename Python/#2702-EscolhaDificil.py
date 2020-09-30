
dados = input()
dados2 = input()
vetor = dados.split()
vetor2 = dados2.split()

Ca = int(vetor[0])
Ba = int(vetor[1])
Pa = int(vetor[2])

Cr = int(vetor2[0])
Br = int(vetor2[1])
Pr = int(vetor2[2])

count = 0

if Cr - Ca > 0:
  count += Cr - Ca
if Br - Ba > 0:
  count += Br - Ba
if Pr - Pa > 0:
  count += Pr - Pa
print(count)
