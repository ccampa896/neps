#include <stdio.h>

int main(){

    float num1, num2, res;

    scanf("%f", &num1);
    scanf("%f", &num2);

    res = ((num1 * 2) + (num2 * 3)) / 5;

    if(res >= 7){
        printf("Aprovado");
    }
    else if(res < 7 && res >= 3){
        printf("Final");
    }
    else{
        printf("Reprovado");
    }

    return 0;
}