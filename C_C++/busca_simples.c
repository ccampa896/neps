#include <stdio.h>

void achou(int vet[10], int procurado);

int main(){

    int vetor[10], i, procurar, res;
    for(i = 0; i < 10; i++){
        scanf("%d", &vetor[i]);
    }

    scanf("%d", &procurar);
    achou(vetor, procurar);

    return 0;
}

void achou(int vet[], int procurado){
    int i = 0, achou = 0;
    while(i < 10){
        if(procurado == vet[i]){
            achou = 1;
            break;
        }
        i++;
    }
    if(achou){
        printf("SIM");
    }
    else{
        printf("NAO");
    }
    

}