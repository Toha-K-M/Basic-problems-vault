#include<stdio.h>

int main(){

int bigmod(int a, int b, int M){
    if(b == 0) return 1%M;
    int x = bigmod(a,b/2,M);
    x = (x*x)%M;
    if(b%2==1) x = (x*a) % M;
    return x;
}

printf("hello world");

int a = 2;
int b = 5;
int M = 3;

printf("%d",bigmod(a,b,M));
return 0;
}

