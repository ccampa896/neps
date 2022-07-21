#include <stdio.h>


int main(){

    int a, b, t1, t2;

    scanf("%d", &a);
    scanf("%d", &b);

    t1 = (a * b) + ((b - 1) * (a - 1));
    t2 = ((b - 1) * 2) + ((a - 1) * 2);

    printf("%d\n%d", t1, t2);

    return 0;
}