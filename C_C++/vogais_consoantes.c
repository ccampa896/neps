#include <stdio.h>
#include <string.h>


int main(){

    char frase[50];
    char vogal[50], consoante[50];
    int z, i = 0, j = 0, tam;

    scanf("%s", frase);

    tam = strlen(frase);

    for(z = 0; z < tam; z++){
        if(frase[z] == 'a'){
            vogal[i] = 'a';
            i++;
        }
        else if(frase[z] == 'e'){
            vogal[i] = 'e';
            i++;
        }
        else if(frase[z] == 'i'){
            vogal[i] = 'i';
            i++;
        }
        else if(frase[z] == 'o'){
            vogal[i] = 'o';
            i++;
        }
        else if(frase[z] == 'u'){
            vogal[i] = 'u';
            i++;
        }
        else{
            consoante[j] = frase[z];
            j++;
        }

        if(z == (tam - 1)){
            vogal[i] = '\0';
            consoante[j] = '\0';
        }
    }

    printf("Vogais: %s\n", vogal);
    printf("Consoantes: %s", consoante);

    return 0;
}