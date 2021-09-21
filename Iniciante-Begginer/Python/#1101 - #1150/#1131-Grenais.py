vitorias_gremio = 0
vitorias_inter = 0
empates = 0
qtd_grenais = 0

while True:
    Gols_do_Inter, Gols_do_Gremio = list(map(int, input().split()))
    qtd_grenais += 1
    if Gols_do_Gremio > Gols_do_Inter:
        vitorias_gremio += 1
    elif Gols_do_Gremio == Gols_do_Inter:
        empates += 1
    else:
        vitorias_inter += 1

    print("Novo grenal (1-sim 2-nao)")
    op = int(input())
    if op == 2:
        break

print('{} grenais'.format(qtd_grenais))
print('Inter:{}'.format(vitorias_inter))
print("Gremio:{}".format(vitorias_gremio))
print("Empates:{}".format(empates))

if vitorias_gremio > vitorias_inter:
    print("Gremio venceu mais")
elif vitorias_gremio < vitorias_inter:
    print("Inter venceu mais")
else:
    print("Nao houve vencedor")
