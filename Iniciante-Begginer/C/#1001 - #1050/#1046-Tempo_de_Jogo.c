// tempo de jogo

#include <stdio.h>

int main()

{

    int hi, et, cont;

    scanf("%d %d", &hi, &et);

    cont = et - hi;

    if (cont < 0)

    {

        cont = 24 + (et - hi);

    }

    if (hi == et)

    {

        printf("O JOGO DUROU 24 HORA(S)\n");

    }

    else printf("O JOGO DUROU %d HORA(S)\n", cont);

 

    return 0;

}
