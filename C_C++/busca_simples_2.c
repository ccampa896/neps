#include <stdio.h>


int main(){

    int vetor[10], inc[10] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1}, i, num, cont = 0;

    for(i = 0; i < 10; i++){
        scanf("%d", &vetor[i]);
    }

    scanf("%d", &num);

    for(i = 0; i < 10; i++){
        if(num == vetor[i]){
            cont++;
            inc[i] = i;
        }
    }

    if(cont != 0){
        printf("%d\n", cont);
        for(i = 0; i < 10; i++){
            if(inc[i] != -1){
                printf("%d ", inc[i]);
            }
        }
    }
    else{
        printf("Mia x");
    }





    return 0; 
}