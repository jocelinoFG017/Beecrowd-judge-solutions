// Salario com bonus

#include <stdio.h>
 
int main() {
 
    char nome;
    
    double salario,vendas,comissao;
 
  scanf("%s %lf %lf", &nome, &salario, &vendas);
 
  comissao = salario + (15*vendas)/100;
 
   printf("TOTAL = R$ %.2f\n",comissao);
 
    return 0;
}
