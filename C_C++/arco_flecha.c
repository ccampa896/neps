#include <stdio.h>

int main(){

	int qtd, i, pena = 0;

	scanf("%d", &qtd);

	for(i = 0; i < qtd; i++){
		float flechas[qtd];
		int x, y;
		float distancia;
		scanf("%d %d", &x, &y);
		distancia = x * x + y * y;
		flechas[i] = distancia;
		int j;
		for(j = 0; j < i; j++){
			if(flechas[j + 1] >= flechas[j]){
				pena++;
			}
		}
	}

	printf("%d", pena);

	return 0;
}
