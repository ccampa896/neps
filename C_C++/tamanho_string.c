#include <stdio.h>
#include <string.h>


int main(){

    char nome[50];
    scanf("%s", nome);
    int tam = strlen(nome);
    printf("%d", tam);

    return 0;
}