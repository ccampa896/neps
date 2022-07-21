#include <stdio.h>


int main(){

    int c[3];
    int igual[3] = {0};

    for(int i = 0; i < 3; i++){
        scanf("%d", &c[i]);
    }

    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            if(i == j){
                continue;
            }
            else if(c[i] == c[j]){
                igual[i] = 1;
                igual[j] = 1;
            }
        }
    }

    for(int i = 0; i < 3; i++){
        if(igual[i] == 0){
            printf("%d\n", c[i]);
        }
    }

    return 0;
}