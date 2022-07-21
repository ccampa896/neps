#include <stdio.h>

class Retangulo{
    int a; //x1
    int b; //y1
    int c; //x2
    int d; //y2

public:
    void set_pontos(int a1, int b1, int a2, int b2){
        a = a1;
        b = b1;
        c = a2;
        d = b2;
    }
    int area(){
        return (c - a) * (b - d);
    }
};

int main(){

    Retangulo retangulo;
    int N;

    scanf("%d", &N);

    for(int i=0;i<N;i++){
        int x1, y1, x2, y2;
        char operacao;

        scanf(" %c", &operacao);

        if(operacao == 'R'){ //Redimensionar
            scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
            retangulo.set_pontos(x1, y1, x2, y2);
        }else if(operacao == 'A'){ //Imprimir a área
            printf("%d\n", retangulo.area());
        }
    }
}
