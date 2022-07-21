#include <stdio.h>


int main(){

	int N, P, Q;
	char operacao;

	scanf("%d", &N);
	scanf("%d %c %d", &P, &operacao, &Q);

	if(operacao == '+'){
		if(P + Q <= N){
			printf("OK");
		}
		else{
			printf("OVERFLOW");
		}
	}
	if(operacao == '*'){
		if(P * Q <= N){
			printf("OK");
		}
		else{
			printf("OVERFLOW");
		}
	}





	return 0;
}
