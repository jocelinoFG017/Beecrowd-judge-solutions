#include <stdio.h>

int main(){

int aux,x;
float numero;

for (x=1; x<=6; x++){
    scanf("%f",&numero);
    if(numero >= 0){
        aux = aux + 1;
    }
}
printf("%d valores positivos\n",aux);

return 0;
}