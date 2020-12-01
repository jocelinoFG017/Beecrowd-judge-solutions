#Author: Jocelino F.G

x = input().split()
a = float(x[0])
b = float(x[1])
c = float(x[2])
d = float(x[3])
media = ((a * 2) + (b * 3) + (c * 4) + (d * 1)) / 10
print('Media: %.1f' %media)
if(media >= 7.0):
  print('Aluno aprovado.')
elif(media < 5.0):
  print('Aluno reprovado.')
elif(media >= 5.0) and (media <=6.9):
  print('Aluno em exame.')
  new = float(input())
  print('Nota do exame: %.1f' %new)
  mediaExame = (new + media) / 2
  if(mediaExame >= 5.0):
    print('Aluno aprovado.')
    print('Media final: %.1f' %mediaExame)
  elif(mediaExame <= 4.9):
    print('Aluno reprovado.')
    print('Media final: %.1f' %mediaExame)
