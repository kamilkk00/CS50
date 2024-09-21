#include <stdio.h>
#include <cs50.h>

int main (void)
{
    while (true)
    {
        int a = 0;
        int i = get_int("Change owed: ");
        if (i > 0)
        {
            while (i >= 25)
            {
                a = a + 1;
                i = i - 25;
            }
            while (i >= 10)
            {
                a = a + 1;
                i = i - 10;
            }
            while (i >= 5)
            {
                a = a + 1;
                i = i - 5;
            }
            while (i >= 1)
            {
                a = a + 1;
                i = i - 1;
            }
            printf("%d\n", a);
            break;
        }
    }

}
