#include <stdio.h>


int main(){

    int x, y;

    scanf("%d", &x);
    scanf("%d", &y);

    if(x == 0 || y == 0){
        printf("eixos");
    }
    else if(x > 0 && y > 0){
        printf("Q1");
    }
    else if(x < 0 && y > 0){
        printf("Q2");
    }
    else if(x < 0 && y < 0){
        printf("Q3");
    }
    else{
        printf("Q4");
    }
    
    return 0;
}