#include <stdio.h>

int main(){
    int i,num, aux =0,posi=0;

    for(i=0;i<100;i++){
        scanf("%d",&num);
        if (num > aux){
            aux = num;
            posi = i+1;
        }
     }
    printf("%d\n",aux);
    printf("%d\n",posi);
return 0;
}