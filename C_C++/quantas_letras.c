#include <stdio.h>
#include <string.h>


int main(){

    char nome[50], letra;
    int qtd = 0, tam, i;

    scanf("%s%*c", nome);
    scanf("%c", &letra);

    tam = strlen(nome);

    for(i = 0; i < tam; i++){
        if(nome[i] == letra){
            qtd++;
        }
    }

    printf("%d", qtd);

    return 0;
}