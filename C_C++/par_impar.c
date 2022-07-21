#include <stdio.h>

void ganhou(int a, int b){
    int res = a + b;
    if(res % 2 == 0){
        printf("Bino");
    }
    else{
        printf("Cino");
    }
}


int main(){

    int bino, cino;
    scanf("%d", &bino);
    scanf("%d", &cino);

    ganhou(bino, cino);


    return 0;
}