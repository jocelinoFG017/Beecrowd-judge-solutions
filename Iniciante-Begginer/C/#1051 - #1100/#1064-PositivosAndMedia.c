#include <stdio.h>

int main(){

double n,soma=0,media;
    int x,y=0;
    for(x=1;x<=6;x++)
    {
        scanf("%lf", &n);
        if(n>=0)
        {
            y++;
            soma+=n;
        }
    }
    media=soma/y;
    printf ("%d valores positivos\n",y);
    printf("%.1lf\n", media);
    return 0;
}