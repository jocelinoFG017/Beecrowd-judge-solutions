#include <stdio.h>

int main(){
    
    double media = 0, soma = 0;
    int idade, count = 0;

    scanf("%d",&idade);

    while( idade > 0){
        count += 1;
        soma = soma + idade;
        media = (soma/count);
        scanf("%d",&idade);
    }
    printf("%.2lf\n",media);
return 0;
}
