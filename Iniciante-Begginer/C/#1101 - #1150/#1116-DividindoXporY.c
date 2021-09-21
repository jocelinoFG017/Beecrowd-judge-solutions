#include <stdio.h>


int main () {

  int n, x, y, i;
  float divisao = 0;
  scanf("%d", &n);


  for (i = 0; i < n; i++)
  {
    scanf("%d %d", &x, &y);
    if (y == 0)
    {

      printf("divisao impossivel\n");

    }
    else
    {

      divisao = (x*1.0)/(y);
      printf("%.1f\n", divisao);

    }
  }
}