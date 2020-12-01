salario = float(input())
ir = 0
renda =0
if (salario >= 0) and (salario <= 2000.00):
    print("Isento")
if (salario >= 2000.01) and (salario <= 3000.00):
    renda = salario - 2000
    ir = (renda * 8) / 100
    print("R$ {:.2f}".format(ir))
if (salario >= 3000.01) and (salario <= 4500.00):
    renda = (8/100) * (1000)
    renda2 = salario - 3000.00
    ir = (renda2 *(18/100)+renda)
    print("R$ {:.2f}".format(ir))
if (salario > 4500.00):
    renda = (8 / 100) * (1000)
    renda2 = (18 / 100) * (1500)
    renda3 = salario - 4500.00
    ir = (renda+renda2+renda3 *(28/100))
    print("R$ {:.2f}".format(ir))
