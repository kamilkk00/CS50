#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int a;
    do
    {
        a = get_int("Height: ");
        a = a + 1;
        if (a < 10)
        {
            for (int i = 1; i < a; i++)
            {
                for (int c = a - 1; c > i; c--)
                    {
                        printf(" ");
                    }
                    for (int b = 0; b < i; b++)
                    {
                        printf("#");
                    }
                    printf("  ");
                    for (int b = 0; b < i; b++)
                    {
                        printf("#");
                    }
                printf("\n");
            }
        }
    }
    while (a < 2 || a > 9);

}
