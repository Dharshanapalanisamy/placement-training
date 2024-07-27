#include <stdio.h>
int main()
{
    int n1, n2;
    printf("Enter the num1 and num2: ");
    scanf("%d", &n1,&n2);
    if ((n1 ^ n2) == 0) {
        printf(" Equal");
    }
    else 
    {
        printf(" Not equal");
    }
}
