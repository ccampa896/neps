#include <stdio.h>

int main(){

    int vet[10], i;

    for(i = 0; i < 10; i++){
        scanf("%d%*c", &vet[i]);
    }

    for(i = 9; i >=0; i--){
        printf("%d\n", vet[i]);
    }

    return 0;
}