#include <stdio.h>

void quick_sort(int vetor[], int tam){
    int i, j, grupo, troca;

    //Critério de parada da recursividade!
    if(tam < 2){
        return; //sai da função
    }else{
    	grupo = vetor[tam / 2];
    }

    //Fazendo um loop único se comportar como dois
    //Veja que estamos utilizando tanto a variável 'i'
    //quanto a variável 'j'.
    //Veja que não temos critério de parada aqui...
    for(i = 0, j = tam - 1;; i++, j--){

    	//Fazemos a movimentação dos elementos no vetor
        while(vetor[i] < grupo){
            i++;
        }

        //Fazemos a movimentação dos elementos no vetor
        while(grupo < vetor[j]){
            j--;
        }
        //Critério de parada do loop
        if(i >= j){
            break;
        }else{
        	//Onde ocorre as trocas
			troca = vetor[i];
			vetor[i] = vetor[j];
			vetor[j] = troca;
        }
    }
    //Usando recursividade para ordenar os grupos
    quick_sort(vetor, i);
    quick_sort(vetor + i, tam - i);
}

int main(){
	
	int n, i, j, aux;
	scanf("%d", &n);
	
	int vetor[n];
	for(i = 0; i < n; i++){
		scanf("%d", &vetor[i]);
	}
	
	quick_sort(vetor, n);

    for(i = 0; i < n; i++){
        printf("%d ", vetor[i]);
    }
	return 0;
}

