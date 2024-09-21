#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        string a = argv[1];
        int x = atoi(argv[1]);
        for (int i = 0, n = strlen(a); i < n; i++)
        {
            if (a[i] < 48 || a[i] > 58)
            {
                printf("./caesar key\n");
                return 1;
                exit(0);

            }
        }
        string zd = get_string("plaintext: ");
        printf("ciphertext: ");
        for (int i = 0, n = strlen(zd); i < n; i++)
        {
            if (zd[i] > 96 && zd [i] < 123)
            {
                zd[i] = zd[i] - 96;
                zd[i] = (zd[i] + x) % 26;
                zd [i] = zd[i] + 96;
            }
            else if (zd[i] > 64 && zd[i] < 91)
            {
                zd[i] = zd[i] - 64;
                zd[i] = (zd[i] + x) % 26;
                zd [i] = zd[i] + 64;
            }
            printf("%c", zd[i]);
        }
        printf("\n");
    }
    else
    {

        printf("./caesar key\n");
        return 1;
    }
}
