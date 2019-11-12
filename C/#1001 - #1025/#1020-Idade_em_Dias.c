//Idade em Dias
#include <stdio.h>

int main(){
	 int age;
	 int y,m,d;

	 scanf("%d",&age);
	 
	 y = age/365;
	 m = (age - (365 * y))/30;
	 d = (age - (365 * y) - (30 * m));
	 
	 printf("%d ano(s)\n",y);
	 printf("%d mes(es)\n",m);
	 printf("%d dia(s)\n",d);

return 0;
}

