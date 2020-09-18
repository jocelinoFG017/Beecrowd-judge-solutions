#Author Jocelino F.G


cod,qtd = map(int, input().split())

if cod == 1:
  total = qtd * 4.00
  print("Total: R$ {:.2f}".format(total))
if cod == 2:
  total = qtd * 4.50
  print("Total: R$ {:.2f}".format(total))
if cod == 3:
  total = qtd * 5.00
  print("Total: R$ {:.2f}".format(total))
if cod == 4:
  total = qtd * 2.00
  print("Total: R$ {:.2f}".format(total))
if cod == 5:
  total = qtd * 1.50
  print("Total: R$ {:.2f}".format(total))
