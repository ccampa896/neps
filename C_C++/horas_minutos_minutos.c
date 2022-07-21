#include <stdio.h>

int main(){

    int h, m, total;

    scanf("%d", &h);
    scanf("%d", &m);

    total = (h * 60) + m;

    printf("%d\n", total);

    return 0;
}