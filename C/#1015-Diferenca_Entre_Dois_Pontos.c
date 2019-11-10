// Distancia entre dois pontos


#include<stdio.h>

#include<math.h>

 

int main()

{

    double x, y, xx, yy, p1, p2, D;

    scanf("%lf %lf %lf %lf", &x, &y, &xx, &yy);

    p1 = xx - x;

    p2= yy - y;

    D = sqrt((p1 * p1) + (p2 * p2));

    printf("%.4lf\n", D);

    return 0;

}
