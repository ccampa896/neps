#include <stdio.h>


int main(){


    int num;

    scanf("%d", &num);

    if(num > 0){
        printf("positivo");
    }
    else if(num < 0){
        printf("negativo");
    }
    else{
        printf("nulo");
    }



    return 0;
}