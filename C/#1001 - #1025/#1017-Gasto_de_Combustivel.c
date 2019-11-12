//Gasto de Combustivel
#include <stdio.h>

int main(){
    int time,vel;
    float lit;
    
    scanf("%d %d",&time,&vel);
    lit = (vel*time)/12.00;
    printf("%.3f\n",lit);
    
return 0;
}

