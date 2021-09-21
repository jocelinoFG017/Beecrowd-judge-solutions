#include <stdio.h>
 
int main() {
    int x, y, soma;
    soma = 0;

    scanf("%d %d",&x, &y);
    
    if ( y > x){
        for(x; x <= y; x++){
            if( x % 13 == 0){
                continue;
            }else{
                soma = soma + x;
            }
        }
    }else{
        for(y; y <= x; y++){
            if( y % 13 == 0){
                continue;
            }else{
                soma = soma + y;
            }
        }
    }
    printf("%d",soma);
    return 0;
}