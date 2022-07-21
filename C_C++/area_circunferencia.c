#include <stdio.h>

#define PI 3.1416

int main(){

	float r, area;

	scanf("%f", &r);

	area = PI * r * r;

	printf("%.2f", area);



	return 0;

}
