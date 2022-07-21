#include <stdio.h>


int main(){

    int n;
    int div = 0;

    scanf("%d", &n);

    for(int i = 1; i <= n; i++){
        if(n % i == 0){
            div += 1;
        }
    }

    if(div == 2){
        printf("Tio\n");
    }
    else{
        printf("Normal\n");
    }

    return 0;
}