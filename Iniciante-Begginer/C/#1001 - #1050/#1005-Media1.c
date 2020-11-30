//media 1
#include <stdio.h>

int main() 
{

   float A, B;
   double MEDIA;

   A = B = 11;

   scanf("%f", &A);
   scanf("%f", &B);

   MEDIA = ((3.5*A) + (7.5*B)) / 11;

   printf("MEDIA = %.5lf\n", MEDIA);

   return (0);
}
