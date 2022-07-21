#include <stdio.h>


int main(){

    int troco, aux, moedas[6] = {0}, i = 0, total = 0;
    scanf("%d", &troco);

    while(troco > 0){
        if(troco >= 100){
            moedas[i] = troco / 100;
            total += moedas[i];
            troco = troco % 100;
        }
        i++;
        if(troco >= 50){
            moedas[i] = troco / 50;
            total += moedas[i];
            troco = troco % 50;
        }
        i++;
        if(troco >= 25){
            moedas[i] = troco / 25;
            total += moedas[i];
            troco = troco % 25;
        }
        i++;
        if(troco >= 10){
            moedas[i] = troco / 10;
            total += moedas[i];
            troco = troco % 10;
        }
        i++;
        if(troco >= 5){
            moedas[i] = troco / 5;
            total += moedas[i];
            troco = troco % 5;
        }
        i++;
        if(troco >= 1){
            moedas[i] = troco / 1;
            total += moedas[i];
            troco = troco % 1;
        }
    }

    printf("%d\n", total);
    for(i = 0; i < 6; i++){
        printf("%d\n", moedas[i]);
    }

    return 0;
}