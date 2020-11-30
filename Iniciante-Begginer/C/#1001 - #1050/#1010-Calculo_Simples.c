//Calculo Simples
#include <stdio.h>

int main()
{
	int cod;
	int num_pecas1;
	float vlr_peca1;
	
	int cod2;
	int num_pecas2;
	float vlr_peca2;
	
	scanf("%d %d %f",&cod,&num_pecas1,&vlr_peca1);
	scanf("%d %d %f",&cod2,&num_pecas2,&vlr_peca2);
	
	printf("VALOR A PAGAR: R$ %.2f\n",(num_pecas1*vlr_peca1)+(num_pecas2*vlr_peca2));
	
	return 0;
}
