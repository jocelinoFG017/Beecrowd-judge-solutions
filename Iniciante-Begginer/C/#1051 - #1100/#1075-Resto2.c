#include <stdio.h>

int main() {
    int i,n;
    scanf("%d",&n);
    i = 1;
    for (i; i< 10001;i++){
        if (i % n == 2){
            printf("%d\n",i);
        }
    }
return 0;
}