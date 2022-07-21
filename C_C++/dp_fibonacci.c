#include <stdio.h>

#define MAX 30
int dp[MAX];

int fib(int n){
    if(dp[n] != 0){
        return dp[n];
    }
    if(n == 0 || n == 1){
        return 1;
    }

    dp[n] = fib(n-1) + fib(n-2);
    return dp[n];


}


int main(){

    int n, res;
    scanf("%d", &n);
    res = fib(n);
    printf("%d", res);





    return 0;
}