#include <stdio.h>

int main(){
    int codigo, senha;
    codigo = 0;
    senha = 2002;

    while(codigo != senha){
        scanf("%d",&codigo);
        if(codigo == senha){
           printf("Acesso Permitido\n");
        }else{
            printf("Senha Invalida\n");
        }
    }
return 0;
}