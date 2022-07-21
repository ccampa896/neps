#include <stdio.h>

int main(){

    int qtd = 0,
    valor;

    scanf("%d", &valor);

    while(valor > 0){
        if(valor >= 100){
            qtd += (valor / 100);
            valor = valor % 100;
        }
        else if(valor >= 50){
            qtd += (valor / 50);
            valor = valor % 50;
        }
        else if(valor >= 25){
            qtd += (valor / 25);
            valor = valor % 25;
        }
        else if(valor >= 10){
            qtd += (valor / 10);
            valor = valor % 10;
        }
        else if(valor >= 5){
            qtd += (valor / 5);
            valor = valor % 5;
        }
        else if(valor >= 1){
            qtd += (valor / 1);
            valor = valor % 1;
        }
    }

    printf("%d", qtd);

    return 0;
}