#include <stdio.h>
int main()
{
    int a , b ;
    printf("Enter the numbers of a and b ");
    scanf("%d %d ",&a,&b);
    printf("max = %d\n", ((a + b) + (a - b)) / 2);
    printf("min = %d\n", ((a + b) - (a - b)) / 2);
}
