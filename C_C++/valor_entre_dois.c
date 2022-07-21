#include <stdio.h>


int main(){

    int a, b, i, maior, menor;

    scanf("%d", &a);
    scanf("%d", &b);

    if(a > b){
        maior = a;
        menor = b;
    }
    else{
        maior = b;
        menor = a;
    }

    for(i = menor; i <= maior; i++){
        printf("%d ", i);
    }

    return 0;
}