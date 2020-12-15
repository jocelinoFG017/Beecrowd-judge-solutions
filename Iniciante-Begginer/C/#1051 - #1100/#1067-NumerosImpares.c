#include <stdio.h>

int main() {
    int i;
    int x ;
    scanf("%d",&x);

    i = 1 ;
    while (i <= x){
      if (i % 2 == 1){
        printf("%d\n",i);
      }
      i = i + 1;

    }
return 0;
}