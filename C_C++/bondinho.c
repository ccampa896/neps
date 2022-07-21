#include <stdio.h>


int main(){

    int a, m;

    scanf("%d", &a);
    scanf("%d", &m);

    if((a + m) > 50){
        printf("N");
    }
    else{
        printf("S");
    }

    return 0;
}