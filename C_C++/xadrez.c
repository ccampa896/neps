#include <stdio.h>

int main(){

    int l, c;

    scanf("%d", &l);
    scanf("%d", &c);

    char l1 = 's';
    char c1 = 's';

    if(l % 2 == 0){
        l1 = 's';
    }
    else{
        l1 = 'n';
    }

    if(c % 2 == 0){
        c1 = 's';
    }
    else{
        c1 = 'n';
    }

    if(l1 == c1){
        printf("%d\n", 1);
    }
    else{
        printf("%d\n", 0);
    }
    
    return 0;
}