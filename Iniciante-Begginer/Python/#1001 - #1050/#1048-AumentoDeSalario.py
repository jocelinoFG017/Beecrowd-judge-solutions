salario = float(input())

if (salario >= 0 ) and (salario <= 400.00):
    novoSalario = salario+((salario * 15) / 100)
    reajuste = (salario * 15) / 100
    print("Novo salario: {:.2f}".format(novoSalario))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 15 %")
if (salario >= 400.01) and (salario <= 800.00):
    novoSalario = salario+((salario * 12) / 100)
    reajuste = (salario * 12) / 100
    print("Novo salario: {:.2f}".format(novoSalario))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 12 %")
if (salario >= 800.01) and (salario <= 1200.00):
    novoSalario = salario+((salario * 10) / 100)
    reajuste = (salario * 10) / 100
    print("Novo salario: {:.2f}".format(novoSalario))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 10 %")
if (salario >= 1200.01) and (salario <= 2000.00):
    novoSalario = salario+((salario * 7) / 100)
    reajuste = (salario * 7) / 100
    print("Novo salario: {:.2f}".format(novoSalario))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 7 %")
if (salario > 2000.00):
    novoSalario = salario + ((salario * 4) / 100)
    reajuste = (salario * 4) / 100
    print("Novo salario: {:.2f}".format(novoSalario))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 4 %")