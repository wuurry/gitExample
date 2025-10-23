#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
    int x1, x2, x3;
    int a1, a2;
    int a, b, c, sa;
    float f1, f2;
    
    printf("\nTo find the arithmetic mean, enter the number of rows:");
    scanf("\n%d", &a);
    for (int i = 0; i < a; i++)
    {
        printf("\nEnter the number of desired numbers in the line");
        scanf("\n%d", &b);
        for (int i = 0; i < b; i++)
        {
            scanf("\n%d", &c);
            sa += c;
        }
        printf("the arithmetic mean: %d", sa / b);
    }
}