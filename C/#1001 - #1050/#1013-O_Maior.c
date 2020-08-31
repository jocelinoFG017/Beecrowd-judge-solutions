// O Maior
#include <stdio.h>
#include <math.h>

int main(){
	int a, b, c;	

	scanf ("%d %d %d", &a, &b, &c);

    int MaiorAB = ((a + b) + fabs(a-b))/2;
    int MaiorABC = ((MaiorAB + c)+fabs(MaiorAB-c))/2;
		
	printf("%d eh o maior\n",MaiorABC); 

	return (0);
}
