#include <stdio.h>

int main(){

	int qtd, a, soma = 0, i;

	scanf("%d", &qtd);

	for(i = 0; i < qtd; i++){
		scanf("%d", &a);
		soma = soma + a;
	}

	printf("%d", soma);


	return 0;
}
