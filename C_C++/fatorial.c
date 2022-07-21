#include <stdio.h>

int fat(int n);

int main(){

    int n, res;
    scanf("%d", &n);
    res = fat(n);
    printf("%d", res);


    return 0;
}

int fat(int n){
    if(n == 0){
        return 1;
    }
    else{
        return n * fat(n-1);
    }
}