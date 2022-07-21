#include <stdio.h>

int main(){

    int teste, cont = 0;

    do{
        scanf("%d", &teste);
        if(teste != 2018){
            cont++;
        }
    }
    while(teste != 2018);

    printf("%d\n", cont);






    return 0;
}