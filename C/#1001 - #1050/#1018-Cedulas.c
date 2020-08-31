#include <stdio.h>

int main()
{
	int N;
	scanf("%d",&N);
	int hun,fifty,twen,ten,five,two,one;
	hun = N/100;
	fifty = (N-(hun*100))/50;
	twen = (N-(hun*100)-(fifty*50))/20;
	ten =  (N-(hun*100)-(fifty*50)-(twen*20))/10;
	five = (N-(hun*100)-(fifty*50)-(twen*20)-(ten*10))/5;
	two = (N-(hun*100)-(fifty*50)-(twen*20)-(ten*10)-(five*5))/2;
	one = (N-(hun*100)-(fifty*50)-(twen*20)-(ten*10)-(five*5)-(two*2))/1;
	
	printf("%d\n",N);
	printf("%d nota(s) de R$ 100,00\n",hun);
	printf("%d nota(s) de R$ 50,00\n",fifty);
	printf("%d nota(s) de R$ 20,00\n",twen);
	printf("%d nota(s) de R$ 10,00\n",ten);
	printf("%d nota(s) de R$ 5,00\n",five);
	printf("%d nota(s) de R$ 2,00\n",two);
	printf("%d nota(s) de R$ 1,00\n",one);
		
	return 0;
}
