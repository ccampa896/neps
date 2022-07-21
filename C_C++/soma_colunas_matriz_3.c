#include <stdio.h>


int main(){

    int m[3][3] = {0}, colunas[3] = {0};

    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            scanf("%d", &m[i][j]);
            colunas[j] += m[i][j];
        }
    }

    for(int i = 0; i < 3; i++){
        printf("Coluna %d: %d\n", i, colunas[i]);
    }
    
    return 0;
}