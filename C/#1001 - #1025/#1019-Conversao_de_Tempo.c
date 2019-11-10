// Conversao de tempo


#include <stdio.h>

int main()
{
 int tempo;

 scanf("%d", &tempo);

 int hora = tempo / 3600;
 tempo = tempo - (hora * 3600);

 int m = tempo / 60;
 tempo = tempo - (m * 60);

 printf("%d:%d:%d\n", hora, m, tempo);

 return 0;
}
